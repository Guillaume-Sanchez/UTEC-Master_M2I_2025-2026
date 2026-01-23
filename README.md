# UTEC-Master_M2I_2025-2026

## Organisation

Horaire : de 9h à 12h30 et de 13h30 à 17h
<details><summary>Tel pro Odile</summary>
<pre>
 06 99 26 53 78
</pre>
</details>


Présentiel et exceptionnellement en distanciel lors des grève etc ...
Autonomie encadrée pour avancer les soutenances et entrepreneuriat
Mobilité à l'international.

Sept 2025 Setp 2026 -> Contrôle continu, pas de partiel

3 soutenances

- Juin : veille Techno (en Groupe, en anglais)
- Juillet : entrepreneuriat (en Groupe, orienté technique en français)
- Septembre : activité Pro (individuelle en français)

## Connexion à Pedagogie CCI sur Linux Récent

Pour ce connecter avec un linux à la Wifi Pedagogie CCI

### Configurer Manuellement IPV4 :

- Adresse : 10.25.32.(150-200)
- Masque : 255.255.255.0
- Passerelle : 10.25.32.1
- DNS : 10.250.56.7

### Onglet sécurité :

- Sécurité : WPA et WPA2 d'entreprise
- Authentification : Protected EAP (PEAP)
- Cocher "Aucun certificat d'AC n'est requis
- Version de PEAP : Automatique
- Autentification interne : MSCHAPv2
- Nom d'utilisateur : mail@cfautec.fr 
- Mot de passe : .... Ton mdp

### Autoriser les vieux algos de chiffrement (Legacy)

Le serveur utilise une version de TLS (SSL) trop vieille pour Debian 13 (OpenSSL 3). Il faut baisser le niveau de sécurité spécifiquement pour cette connexion.

#### Modifions le fichier de configuration directement :

Ouvrez le fichier de connexion en root :

```Bash
sudo vim "/etc/NetworkManager/system-connections/Pedagogie CCI.nmconnection"
```
>(Note : Si le fichier n'est pas trouvé, faites un `ls /etc/NetworkManager/system-connections/` pour trouver le nom exact).

#### Cherchez la section [802-1x].

Ajoutez (ou modifiez) cette ligne à la fin de cette section :

```
phase1-auth-flags=32
```

(Le code 32 indique au système d'autoriser le TLS 1.0, souvent requis sur les vieux serveurs RADIUS).

#### Rechargez la configuration :

```Bash
sudo nmcli connection reload
sudo nmcli connection up "Pedagogie CCI"
```