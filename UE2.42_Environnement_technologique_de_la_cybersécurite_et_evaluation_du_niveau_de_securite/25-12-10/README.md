# 25 12 10

Attention à ne pas confondre VLAN et Sous-réseau

## TP 1 

Comment protéger ce réseau :

- Ségmentation 
- DMZ : On y met les réseau qui a besoin d'$être joignable par internet. Si il y a piratage, la MDZ permet de limiter l'accès au pirate qu'aux machines présentes dans la DMZ.
- Private VLAN : permet de définir vos Vlan dans des sous groupe (Community isolated promiscuous)
- Réseau Secrétaire
- Réseau Développeur
- Réseau Admin (Bastion)
- Réseau Serveurs
- FireWall (Tout fermer : Ouvrir uniquement les ports necessaires) (Tout ouvert : Sauf ce qui est interdit)

***Schéma*** :

![TD1-Analyse.png](./TD1-Analyse.png)

***Tableaux des protocoles*** :

| Action | Source | Destination | Protocole | Port |
| :----: | :----: | :---------: | :-------: | :--: |
| pass | Secretaire | HTTP | TCP | 80 |
| pass | DNS | SMTP | TCP | 25 |
| pass | Secretaire | HTTPS | TCP | 443 |
| pass | NTP | SMTP | TCP | 25 |
| pass | HTTP | SMTP | TCP | 25 |
| pass | FTP | SMTP | TCP | 25 |
| pass | Admin | VLAN 10,20,30,40,50 | TCP,UDP | Any |
| pass | Admin | VLAN 10,20,30,40,50 | ICMP | Any |
| pass | Dev | HTTPS | TCP | 443 |
| pass | Dev | HTTP | TCP | 80 |
| pass | Dev | DNS | UDP | 53 |
| pass | Dev | NTP | TCP | 123 |
| block | Dev | FTP | TCP | 22 |
| pass | Dev | FTP | TCP | Any |
| pass | Secretaire | DNS | UDP | 53 |
| pass | Secretaire | NTP | TCP | 123 |
| pass | DNS2 | DNS | TCP | 53 |
| pass | DNS2 | NTP | UDP | 123 |
| pass | HTTPS | NTP | UDP | 123 |
| pass | SMTP | NTP | UDP | 123 |
| pass | DNS | Internet | UDP | 53 |
| pass | NTP | Internet | UDP | 123 |
| pass | UPDATE | Internet | TCP | (Mise à jour) |
| pass | DNS2, HTTPS, SMTP | UPDATE | TCP | (Mise à jour) |
| pass | Internet | HTTPS | TCP | 443 |
| block | any |	any | any |	any |

***Protection contre les attaques*** :

- Server qui ne sert à rien ou Honypot
- Protection de DHCP -> DHCP Spoofing
