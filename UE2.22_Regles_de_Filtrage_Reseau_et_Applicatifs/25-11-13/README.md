# TP Filtrage de paquets

## Politique de filtrage par défaut

1. Lancer la commande iptables -L puis observer la sortie d’écran. 

```
root@U2-22:~/regles_filtrages# iptables -L
Chain INPUT (policy ACCEPT)
target     prot opt source               destination         

Chain FORWARD (policy ACCEPT)
target     prot opt source               destination         

Chain OUTPUT (policy ACCEPT)
target     prot opt source               destination 
```

2. Quelle est la politique adoptée par chacune des chaînes prédéfinies ? 

Tout peux rentrer et tou peux sortir


## Exploitation des règles de filtrage

1. Créer sur le poste Serveur un répertoire nommé « firewall ». 

2. Copier dans ce répertoire le fichier regles-filtrage.tar.gz puis décompacter le avec la commande « tar xvzf regles-filtrage.tar.gz ». Vous devez obtenir les fichiers scripts suivants : deny-all, accept-all, block-ip et unblock-ip. 

3. Rendre ces fichiers exécutables (droits d’accès 700). 

4. Exécuter le script deny-all en tapant « ./deny-all ». Essayer de faire un ping localhost et 192.168.10.254. Que constatez-vous ? Décrivez les règles utilisées par ce script. 

Le ping fonctionne car aucune règles n'est appliqué.

5. Editer le script deny-all puis décommenter les lignes suivantes : 

```
#INTERFACE_LOOPBACK=lo 
#iptables -A OUTPUT –o $INTERFACE_LOOPBACK –j ACCEPT 
#iptables -A INPUT –i $INTERFACE_LOOPBACK –j ACCEPT 
```

6. Exécuter le script obtenu puis ressayer à nouveau les deux commandes Ping précédentes. Que constatez-vous cette fois ci ? Expliquez.  

Le ping ne fonctionne plus, en effet les règles décommenté empêche les entrées et les sorties.

7. Afficher les informations concernant les paquets examinés par le pare-feu en 
utilisant la commande « iptables –L -v». Commenter la sortie d’écran.  

```
root@U2-22:~# iptables -L -v
Chain INPUT (policy DROP 15 packets, 2404 bytes)
 pkts bytes target     prot opt in     out     source               destination         
    0     0 ACCEPT     all  --  lo     any     anywhere             anywhere            

Chain FORWARD (policy DROP 0 packets, 0 bytes)
 pkts bytes target     prot opt in     out     source               destination         

Chain OUTPUT (policy DROP 8 packets, 880 bytes)
 pkts bytes target     prot opt in     out     source               destination         
    0     0 ACCEPT     all  --  any    lo      anywhere             anywhere 
```

8. Exécuter le script  accept-all en tapant « ./accept-all » puis essayer de faire 
un ping localhost et 192.168.10.254. Que constatez-vous ? Décrivez les règles utilisées par ce script. 

```
root@U2-22:~/regles_filtrages# ./accept-all

root@U2-22:~/regles_filtrages# iptables -L -v 
Chain INPUT (policy ACCEPT 6 packets, 896 bytes)
 pkts bytes target     prot opt in     out     source               destination         

Chain FORWARD (policy ACCEPT 0 packets, 0 bytes)
 pkts bytes target     prot opt in     out     source               destination         

Chain OUTPUT (policy ACCEPT 2 packets, 256 bytes)
 pkts bytes target     prot opt in     out     source               destination 
```

il n'y a plus aucune règle de deny donc tout est de nouveau ouvert.

9. Exécuter le script block-ip en tapant « ./block-ip 192.168.10.254 ». Essayer maintenant  de  faire  un  ping  localhost  et  192.168.10.254.  Que  constatez-vous ? Décrivez les règles utilisées par ce script. 



10. Exécuter le script unblock-ip en tapant « ./unblock-ip 192.168.10.254 » puis essayer de faire un ping localhost et 192.168.10.254. Que constatez-vous ? Décrivez les règles utilisées par ce script. 

## réation de nouvelles règles de filtrage

1. Interdire un paquet s’il ne provient pas de localhost 

`iptables -A INPUT ! -i lo -d 127.0.0.1 -j DROP`

2. Interdire le protocole ICMP à destination de localhost 

`iptables -A INPUT -p icmp -d 127.0.0.1 -j DROP`

3. Interdire tout paquet à destination du port Telnet 

`iptables -A INPUT -p tcp --dport 23 -j DRO`

4. Interdire tout paquet sortant par eth0 dont le numéro du port destination est inférieur à 1024 

`iptables -A OUTPUT -o eth0 -p tcp --dport 0:1023 -j DROP`
`iptables -A OUTPUT -o eth0 -p udp --dport 0:1023 -j DROP`

5. Interdire toute tentative d’initialisation de connexion TCP provenant de eth0  

`iptables -A INPUT -i eth0 -p tcp --syn -j DROP`

6. Interdire toute réponse à un Ping 

`iptables -A OUTPUT -p icmp --icmp-type echo-reply -j DROP`

7. Interdire tout paquet entrant par eth0 dont l’adresse mac n’est pas celle du poste de travail (voir le schéma à la page 1) Remarque : Attention, vous ne pouvez utiliser le filtrage par adresse mac que sur la table INPUT 

`iptables -A INPUT -i eth0 -m mac --mac-source 28:3a:4d:46:6a:8f -j ACCEPT`
`iptables -A INPUT -i eth0 -j DROP`

8. Interdire  les  paquets  provenant  du  sous-réseau  local  192.168.10.0/24  sauf ceux en provenance du poste de travail. Remarque : Vous devez utiliser, dans ce cas, deux règles de filtrage. Appliquer ces règles puis essayer d’établir depuis le poste de travail, une connexion  FTP  vers  le  pare-feu.  Inversez  l’ordre  de  ces  deux  règles  puis réessayez l’opération. Que remarquez-vous ? Quelle conclusion pouvez-vous en tirer ? 

***Cas 1 : Ordre correct (autorisation avant interdiction)***

```
# 1. Autoriser le poste de travail
iptables -A INPUT -s 192.168.10.5 -j ACCEPT

# 2. Interdire le reste du sous-réseau
iptables -A INPUT -s 192.168.10.0/24 -j DROP
```

- Le poste 192.168.10.5 peut accéder au pare-feu (ex. via FTP).
- Tous les autres hôtes du réseau 192.168.10.0/24 sont bloqués.

***Cas 2 : Ordre inversé (interdiction avant autorisation)***

```
# 1. Interdire le sous-réseau
iptables -A INPUT -s 192.168.10.0/24 -j DROP

# 2. Autoriser le poste de travail
iptables -A INPUT -s 192.168.10.5 -j ACCEPT
```

Le poste 192.168.10.5 est aussi bloqué !

En effet, iptables lit les règles dans l’ordre, et la première règle correspondante est appliquée immédiatement. Donc le paquet venant de 192.168.10.5 correspond déjà à la règle de DROP du réseau entier, et ne va jamais jusqu’à la règle ACCEPT.

9. Écrire  une  règle  qui  laisse  passer  5  tentatives  de  connexion  TCP  avec  une fréquence de 2 tentatives par minute. 

`iptables -A INPUT -p tcp --syn -m limit --limit 2/minute --limit-burst 5 -j ACCEPT`
`iptables -A INPUT -p tcp --syn -j DROP`

10. Créer  une  nouvelle  chaîne  qui  journalise  puis  rejette  tout  paquet  qui  la traverse.  Les  paquets  journalisés  doivent  être  précédés  par  le  préfixe [FIREWALL  DROP].  Renvoyer  ensuite  sur  cette  nouvelle  chaîne  tout  paquet entrant qui demande l’établissement d’une nouvelle connexion.

11. Positionnez la politique de filtrage par défaut à DROP pour les trois chaînes prédéfinies 

12. Autoriser  tout  paquet  sortant  relatif  à  une  connexion  déjà  établie  ou  en rapport avec une connexion déjà établie 

13. Interdire tout paquet sortant relatif à une connexion de type INVALID 

14. Autoriser tout paquet créant une nouvelle connexion en entrée à destination du port 80 

15. Utiliser le navigateur web du poste de travail pour accéder à l’adresse URL « http://www.network.net/site ». Que constatez-vous ? 

16. A présent, essayer l’adresse URL suivante « http://192.168.10.2/site ». Que constatez-vous cette fois ci ? Un problème qui se pose. Lequel ?  

17. Que doit-on faire pour le résoudre ?

## Analyse d’un script de filtrage

1. Expliquer pour chaque partie, les règles utilisées et leur rôle. 

2. Réaliser  pour  chaque  partie  les  tests  qui  permettent  d’en  vérifier  le  bon fonctionnement. Inclure dans le rapport la sortie et/ou les captures d’écran des différentes commandes utilisées lors des tests. 
 
3. Selon  le  script  précédent,  dire  où  se  situe  exactement  le  pare-feu  dans l’architecture réseau qu’il protège puis donner une description générale de la protection qu’il permet d’assurer.  