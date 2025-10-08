#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ipv4_calc.py
Calculatrice IPv4 (fonctions clés du site site24x7 ipv4 subnet calculator)
Usage:
    python ipv4_calc.py 192.168.1.10/24
    python ipv4_calc.py 10.0.5.7 255.255.255.0
    python ipv4_calc.py --split 192.168.0.0/22 --subnet-size 24   # découper /22 en /24
    python ipv4_calc.py --by-hosts 192.168.0.0/24 --hosts 50      # trouver préfixe nécessaire
"""
from __future__ import annotations
import ipaddress
import argparse
import math
from typing import Tuple, List


def ip_to_bin_str(ip: ipaddress.IPv4Address) -> str:
    return '.'.join(f'{octet:08b}' for octet in ip.packed)


def mask_to_wildcard(mask: ipaddress.IPv4Address) -> ipaddress.IPv4Address:
    # wildcard = inverse of mask
    mask_int = int(mask)
    wildcard_int = (~mask_int) & 0xFFFFFFFF
    return ipaddress.IPv4Address(wildcard_int)


def usable_host_count(prefixlen: int) -> int:
    if prefixlen == 32:
        return 1  # only the host itself
    if prefixlen == 31:
        return 2  # RFC 3021: two-host point-to-point networks (no broadcast)
    return max(0, (1 << (32 - prefixlen)) - 2)


def summarize_network(network: ipaddress.IPv4Network) -> dict:
    net_addr = network.network_address
    broadcast = network.broadcast_address
    prefixlen = network.prefixlen
    netmask = network.netmask
    wildcard = mask_to_wildcard(netmask)
    total_hosts = (1 << (32 - prefixlen))
    usable = usable_host_count(prefixlen)

    # first/last usable host (handle /31 and /32 specially)
    if prefixlen == 32:
        first_usable = last_usable = net_addr
    elif prefixlen == 31:
        # two addresses, both usable (RFC 3021)
        first_usable = net_addr
        last_usable = network.network_address + 1
    else:
        first_usable = net_addr + 1
        last_usable = broadcast - 1

    return {
        'network': str(net_addr),
        'cidr': f'{net_addr}/{prefixlen}',
        'netmask': str(netmask),
        'netmask_binary': ip_to_bin_str(netmask),
        'wildcard': str(wildcard),
        'wildcard_binary': ip_to_bin_str(wildcard),
        'broadcast': str(broadcast),
        'first_usable': str(first_usable),
        'last_usable': str(last_usable),
        'total_hosts': total_hosts,
        'usable_hosts': usable,
        'prefixlen': prefixlen,
        'network_binary': ip_to_bin_str(net_addr),
    }


def parse_input(ip_str: str, mask_str: str = None) -> ipaddress.IPv4Network:
    """
    Accept:
      - "192.168.1.10/24"
      - "192.168.1.10 255.255.255.0"
      - "192.168.1.0/24"
    Returns an IPv4Network object (network derived from given IP and mask).
    """
    if '/' in ip_str:
        # ip/prefix form
        iface = ipaddress.IPv4Interface(ip_str)
        return iface.network
    else:
        # ip + mask form or ip alone -> require mask_str
        if mask_str is None:
            raise ValueError("Masque non fourni. Utiliser format 'IP/PREFIX' ou fournir le masque.")
        # If mask_str is like /24, remove slash
        if mask_str.startswith('/'):
            mask_str = mask_str[1:]
        # If mask_str is decimal prefix
        if mask_str.isdigit():
            prefix = int(mask_str)
            iface = ipaddress.IPv4Interface(f"{ip_str}/{prefix}")
            return iface.network
        # Otherwise assume dotted mask
        try:
            # compute prefix from mask
            mask_ip = ipaddress.IPv4Address(mask_str)
            # translate to prefixlen:
            mask_int = int(mask_ip)
            prefix = mask_int.bit_count()  # number of ones
            iface = ipaddress.IPv4Interface(f"{ip_str}/{prefix}")
            return iface.network
        except Exception as e:
            raise ValueError(f"Masque invalide: {mask_str}") from e


def split_network_into_prefix(network: ipaddress.IPv4Network, new_prefix: int) -> List[ipaddress.IPv4Network]:
    if new_prefix < network.prefixlen:
        raise ValueError("new_prefix doit être >= prefix du réseau d'origine")
    return list(network.subnets(new_prefix=new_prefix))


def required_prefix_for_hosts(hosts: int) -> int:
    """
    Retourne le préfixe minimal capable de contenir 'hosts' hôtes utilisables.
    Pour hosts <= 2, /31 ou /32 peuvent être envisagés.
    """
    if hosts <= 0:
        raise ValueError("Le nombre d'hôtes doit être positif.")
    # handle /32 -> 1, /31 -> 2, others -> usable = 2^(32-p)-2
    if hosts == 1:
        return 32
    if hosts == 2:
        return 31
    # find minimal p such that (2^(32-p) - 2) >= hosts
    # => 2^(32-p) >= hosts + 2
    needed = hosts + 2
    power = math.ceil(math.log2(needed))
    prefix = 32 - power
    if prefix < 0:
        raise ValueError("Trop d'hôtes demandés pour IPv4")
    return prefix


def pretty_print_summary(s: dict):
    print(f"Réseau : {s['cidr']} ({s['network']})")
    print(f"Masque  : {s['netmask']}  (/{s['prefixlen']})")
    print(f"Masque (binaire): {s['netmask_binary']}")
    print(f"Wildcard: {s['wildcard']}  (binaire: {s['wildcard_binary']})")
    print(f"Adresse de broadcast : {s['broadcast']}")
    print(f"Plage hôtes utilisables : {s['first_usable']} - {s['last_usable']}")
    print(f"Total adresses : {s['total_hosts']}   |  Hôtes utilisables : {s['usable_hosts']}")
    print(f"Adresse réseau (binaire) : {s['network_binary']}")
    print()


def main():
    parser = argparse.ArgumentParser(description="Calculatrice IPv4 (subnet calculator)")
    parser.add_argument('ip', help="IP ou réseau. Ex: 192.168.1.10/24 ou 10.0.0.1")
    parser.add_argument('mask', nargs='?', default=None, help="Masque (optionnel si 'ip' contient /). Ex: 255.255.255.0 ou /24")
    parser.add_argument('--split', action='store_true', help="Afficher la liste des sous-réseaux")
    parser.add_argument('--subnet-size', type=int, default=None, help="Si --split: nouveau préfixe (ex: 24)")
    parser.add_argument('--by-hosts', action='store_true', help="Calculer le préfixe nécessaire pour un nombre d'hôtes (utiliser --hosts)")
    parser.add_argument('--hosts', type=int, default=None, help="Nombre d'hôtes (utile avec --by-hosts)")
    args = parser.parse_args()

    # by-hosts mode
    if args.by_hosts:
        if args.hosts is None:
            parser.error("--by-hosts nécessite --hosts N")
        prefix = required_prefix_for_hosts(args.hosts)
        print(f"Pour {args.hosts} hôtes utilisables, préfixe minimal: /{prefix}")
        print(f"Taille réseau: {1 << (32 - prefix)} adresses totales, {usable_host_count(prefix)} hôtes utilisables")
        return

    try:
        network = parse_input(args.ip, args.mask)
    except Exception as e:
        parser.error(str(e))

    summary = summarize_network(network)
    pretty_print_summary(summary)

    if args.split:
        if args.subnet_size is None:
            parser.error("--split nécessite --subnet-size")
        new_pref = args.subnet_size
        subnets = split_network_into_prefix(network, new_pref)
        print(f"Découpage de {network.with_prefixlen} en /{new_pref} : {len(subnets)} sous-réseaux")
        for s in subnets:
            summ = summarize_network(s)
            print(f" - {s.with_prefixlen}: {summ['first_usable']} - {summ['last_usable']} (utilisables: {summ['usable_hosts']})")


if __name__ == "__main__":
    main()