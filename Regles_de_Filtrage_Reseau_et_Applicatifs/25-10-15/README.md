***Pour bloquer toutes les connexions TCP***

R1 :

access-list 101 deny tcp host 192.168.20.1
host 192.168.40.1

***Activer acl dans l'interface GO/1***

ip access-group 101 in

***Autoriser uniquement le PC4 d'accèder au serveur 0 en FTP***

access-list 101 deny tcp host 192.168.20.1
