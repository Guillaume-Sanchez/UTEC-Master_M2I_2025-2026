# Commande de base Switch Cisco

## 🔧 1. Accéder au mode privilégié

```
Switch> enable
```

> Passe en mode privilégié (niveau supérieur de commande).

## ⚙️ 2. Entrer en mode de configuration globale

```
Switch# configure terminal
```

## 🕵️ 3. Définir le nom du switch

```
Switch(config)# hostname NomSwitch
```

## 🔒 4. Configurer un mot de passe pour le mode privilégié

```
NomSwitch(config)# enable password votre_mot_de_passe
```

👉 Ou (plus sécurisé) :

```
NomSwitch(config)# enable secret votre_mot_de_passe
```

## 🔐 5. Sécuriser l’accès en console

```
NomSwitch(config)# line console 0
NomSwitch(config-line)# password votre_mot_de_passe
NomSwitch(config-line)# login
NomSwitch(config-line)# exit
```

##  📡 6. Configurer les lignes VTY (accès distant : Telnet/SSH)

```
NomSwitch(config)# line vty 0 15
NomSwitch(config-line)# password votre_mot_de_passe
NomSwitch(config-line)# login
NomSwitch(config-line)# transport input telnet ssh
NomSwitch(config-line)# exit
```

## 🔧 7. Configurer une interface VLAN pour l’administration (ex: VLAN 1)

```
NomSwitch(config)# interface vlan 1
NomSwitch(config-if)# ip address 192.168.1.2 255.255.255.0
NomSwitch(config-if)# no shutdown
NomSwitch(config-if)# exit
```

## 🔧 7Bis. Configurer d'un Vlan


Création d'un VLAN
```
vlan "numéro_vlan"
```
Affesctation d'un VLAN à un groupe d'interfaces
```
interface range Fa0/"min - max"
    switchport mode access
    switchport access vlan "numéro_vlan"
```
Configuration d'un port en agrégation de VLAN 802.1Q
```
interface "nom_interface"
    switchport mode trunk
```

Pour vérifier les interfaces VLAN 

```
! Affiche la liste des VLAN
show vlan
! Affiche les agrégations de VLAN
show interface trunk
```

## 🌐 8. Définir la passerelle par défaut

```
NomSwitch(config)# ip default-gateway 192.168.1.1
```

## 👥 9. Créer un compte utilisateur (recommandé pour SSH)

```
NomSwitch(config)# username admin password votre_mot_de_passe
```

## 🔐 10. Activer et configurer SSH (optionnel mais recommandé)

```
NomSwitch(config)# ip domain-name monreseau.local
NomSwitch(config)# crypto key generate rsa
# Choisir une taille de clé (ex: 1024 ou 2048)

NomSwitch(config)# line vty 0 15
NomSwitch(config-line)# login local
NomSwitch(config-line)# transport input ssh
NomSwitch(config-line)# exit
```

## 💾 11. Sauvegarder la configuration

```
NomSwitch# write memory
# ou
NomSwitch# copy running-config startup-config
```

## ✅ 12. Vérification (commandes utiles)

- Voir la configuration en cours :

```
NomSwitch# show running-config
```

- Vérifier les interfaces :

```
NomSwitch# show ip interface brief
```

- Voir les VLANs :

```
NomSwitch# show vlan brief
```