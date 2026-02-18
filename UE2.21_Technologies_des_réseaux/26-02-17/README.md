# Rappel 2024

## Exercice 3

Il s'agit d'une requête HTTP GET (navigation web) envoyée par l'hôte 172.16.0.100 vers le serveur web 172.16.0.2

Ethernet :
------

00 50 FC 20 3A 4A : Adresse Mac Desination

00 50 FC 0B 9A 80 : Adresse Mac Source

08 00 : Type de la Trame 

IP :
------

4 : Le datagrame contenu correspond à la version 4 d'IP

5 : 5 * 4 = 20 octets, l'entête IP fait 20 octets de longuer

00 : Vide

01 3E : Longueur de la trame IP ()

8E 4F : Identification

40 00 : Fragment offset 0 donc pas de fragment

80 : Time to live (128)

06 : Numéro du protocole, 06 correspond au protocole TCP

12 E4 : ?

AC 10 00 64 : IP Source 172.16.0.100

AC 10 00 02 : IP Destination 172.16.0.2

TCP :
------

19 32 : Port Source 6450

00 50 : Port Destination 80 (http)

2C 3D 86 A1 : Numéro de séquence absolu

92 D3 19 AD : Acknowledgement number

50 : 

18 : Flags

FA F0 : 

1F 2F :

00 00 : 