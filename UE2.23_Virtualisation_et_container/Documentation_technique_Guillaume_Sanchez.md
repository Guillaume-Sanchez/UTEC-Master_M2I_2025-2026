# Documentation technique Guillaume Sanchez
| Version | Date | Commentaire |
|:--:|:--:|:--:|
| 1.0 | 17/12/2025 | Première version de la documentation |
| 2.0 | 22/01/2025 | Modification des scripts par des repos git |

```
1 - Primo-Installation
	1.1 - Prérequis
		1.1.1 - Mise à jour et installation des outils divers
		1.1.2 - Création d'un utilisateur et restriction de l'utilisation du compte
		root à la connexion ssh
		1.1.3 - Installation de Docker
	  	1.1.3.1 - Installez le Référentiel apt de Docker.
	  	1.1.3.2 - Installez les paquets Docker
			1.1.3.3 - Gestion du service Docker
		1.1.4 - Installation de Portainer
			1.1.4.1 - Prérequis
			1.1.4.2 - Installez Portainer avec Docker
			1.1.4.3 - Accéder au portail Portainer
		1.1.5 - Initialisation de l'environnement kactus
	1.2 - Mise en place des Stacks
		1.2.1 - Première connexion au portainer
		1.2.2 - Stack kactus-inta
		1.2.3 - Stack kactus-web
		1.2.4 - Stack monitoring
		1.2.5 - Stack php_ip_am
		1.2.6 - Stack npm
```

Mise en place d'un environnement docker des services de l'entreprise Kactus
> Cette Documentation est valable sur une machine sous la distribution Debian 13

## 1 - Primo-Installation
### 1.1 - Prérequis
#### 1.1.1 - Mise à jour et installation des outils divers
Mise à jour du système :
```bash
apt update && apt upgrade -y
```
Installation de sudo, git, zip, vim, curl
```
apt install -y git sudo zip vim curl
```
#### 1.1.2 - Création d'un utilisateur et restriction de l'utilisation du compte root à la connexion ssh
Création du compte administrateur :
```bash
adduser admkactus
usermod -aG sudo admkactus
```
Modification du fichier `sshd_config` pour empêcher l'utilisation du compte root pour une connexion en ssh :
```bash
sed -i 's/^#\?PermitRootLogin.*/PermitRootLogin no/' /etc/ssh/sshd_config
systemctl restart ssh
```
>Utiliser le compte `admkactus` pour tout le reste de cette documentation 
```bash
su - admkactus
```
#### 1.1.3 - Installation de Docker
##### 1.1.3.1 - Installez le Référentiel `apt` de Docker.
```bash
# Add Docker's official GPG key:
sudo apt install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
sudo tee /etc/apt/sources.list.d/docker.sources <<EOF
Types: deb
URIs: https://download.docker.com/linux/debian
Suites: $(. /etc/os-release && echo "$VERSION_CODENAME")
Components: stable
Signed-By: /etc/apt/keyrings/docker.asc
EOF
sudo apt update
```
##### 1.1.3.2 - Installez les paquets Docker
```bash
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin 
docker-compose-plugin
```
##### 1.1.3.3 - Gestion du service Docker
Pour vérifier le status des services docker :
```bash
sudo systemctl status docker
```
Pour démarrer les services docker :
```bash
sudo systemctl start docker
```
Pour stopper les services docker :
```bash
sudo systemctl stop docker
```
Pour redémarrer les services docker :
```bash
sudo systemctl restart docker
```
Pour désactiver le lancement des services docker au démarrage de la :
```bash
sudo systemctl disable docker
```
Pour activer le lancement des services docker au démarrage de la :
```bash
sudo systemctl enable docker
```
#### 1.1.4 - Installation de Portainer
##### 1.1.4.1 - Prérequis
Avoir Docker
##### 1.1.4.2 - Installez Portainer avec Docker
Pour installer Portainer, exécutez les commandes suivantes :
```bash
sudo docker volume create portainer_data
sudo docker run -d -p 9000:9000 --name=portainer --restart=always -v /var/run/docker.sock:
/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce
```
Voici ce que cette commande fait :
- Crée un volume Docker portainer_data pour stocker les données de Portainer de manière persistante.
- Démarre un nouveau conteneur Docker nommé portainer qui exécute Portainer, configuré pour redémarrer automatiquement.
- Expose le port 9000, sur lequel l’interface utilisateur web de Portainer sera accessible.
- Montre le socket Docker dans le conteneur, permettant à Portainer de gérer les conteneurs sur l’hôte Docker.
##### 1.1.4.3 - Accéder au portail Portainer
Une fois Portainer lancé, vous pouvez accéder à l’interface utilisateur :
[http://votre_adresse_ip_serveur:9000](http://localhost:9000)
Sur la page d’accueil de Portainer, vous serez invité à créer un utilisateur administrateur. Remplissez les détails demandés et connectez-vous.
#### 1.1.5 - Initialisation de l'environnement kactus
>sur l'hyperviseur, en tant que admkactus :
Lancer la commande de là primo-installation du script à distance disponible sur le repo Git du projet.
```bash
cd ~
bash -c "$(curl https://raw.githubusercontent.com/Guillaume-Sanchez/kactus/refs/heads/
main/script/primo_install.sh)"
```
Voici ce que ce script fait :
- Il clone le repo git du projet dans `/home/admkactus/`.
- Si le clonage, c'est bien déroulé, il place les fichiers de configurations de prometheus, promail, phpIPAM et wordpress dans `/opt/kactus/`.
- Il met en place une crontab pour générer des rapports trivy.
- Il créer le réseau kactus-network.
>En cas d'impossibilité de lancer la commande à distance, récupérer le script sur le [ici](https://github.com/Guillaume-Sanchez/kactus/blob/main/script/primo_install.sh), le placer sur l'hyperviseur et le lancer. 

En cas de problème, une documentation primaire est présente sur le repos Git : [Repos Kactus](https://github.com/Guillaume-Sanchez/kactus)

### 1.2 - Mise en place des Stacks
L'infra est séparé en plusieurs Stacks qu'il faut mettre en place et relier au repot git afin de pouvoir gérer le CI/CD de l'infra.
Pour cela, il faut se connecter sur portainer avec un compte administrateur.
#### 1.2.1 - Première connexion au portainer
- Choisir un nom de compte pour créer un administrateur.
- Mettre un mot de passe robuste.

Pour créer les stacks, il faut se rendre dans l'onglet `Stacks` 
Puis cliquer sur `+ Add stack`
#### 1.2.2 - Stack `kactus-inta`
Dans l'onglet `build method`, cliquer sur `Repository`.
Rentrer les informations suivantes pour lier le repo Git à cette stack :
- Name : `kactus-inta`
- Repository URL : `https://github.com/Guillaume-Sanchez/kactus.git`
- Repository reference : `refs/heads/main`
- Compose path : `kactus-inta/docker-compose.yml`
- Activer `GitOps updates` et laisser sur `polling`

Pour finir, cliquer sur `Deploy the stcak`
> Si un problème survient, vérifier les informations entrées et que les fichiers de configuration soit bien placé dans `/opt/kactus/` sur l'hypervisor suite au passage du script de primo-install (se référer au point 1.1.5 de cette documentation).

#### 1.2.3 - Stack `kactus-web`
Dans l'onglet `build method`, cliquer sur `Repository`.
Rentrer les informations suivantes pour lier le repo Git à cette stack :
- Name : `kactus-web`
- Repository URL : `https://github.com/Guillaume-Sanchez/kactus.git`
- Repository reference : `refs/heads/main`
- Compose path : `kactus-web/docker-compose.yml`
- Activer `GitOps updates` et laisser sur `polling`
- Ajouter 6 variables d’environnement en cliquant sur `+ Add an environment variable` :
	-  MYSQL_ROOT_PASSWORD : `Mot_de_passe_root_de_la_BDD`
	- MYSQL_DATABASE : `wordpress`
	- MYSQL_USER : `kactus`
	- MYSQL_PASSWORD : `Mot_de_passe_de_la_BDD`
	- WORDPRESS_DB_USER : `kactus`
	- WORDPRESS_DB_PASSWORD : `Mot_de_passe_de_la_BDD`

Pour finir, cliquer sur `Deploy the stcak`
> Si un problème survient, vérifier les informations entrées et que les fichiers de configuration soit bien placé dans `/opt/kactus/` sur l'hypervisor suite au passage du script de primo-install (se référer au point 1.1.5 de cette documentation).
Pour finir, cliquer sur `Deploy the stcak`
#### 1.2.4 - Stack `monitoring`
Dans l'onglet `build method`, cliquer sur `Repository`.
Rentrer les informations suivantes pour lier le repo Git à cette stack :
- Name : `monitoring`
- Repository URL : `https://github.com/Guillaume-Sanchez/kactus.git`
- Repository reference : `refs/heads/main`
- Compose path : `monitoring/docker-compose.yml`
- Activer `GitOps updates` et laisser sur `polling`
- Ajouter 2 variables d’environnement en cliquant sur `+ Add an environment variable` :
	-  GRAFANA_ADMIN : `admin`
	- GRAFANA_PASSWORD : `Mot_de_passe_admin`

Pour finir, cliquer sur `Deploy the stcak`
> Si un problème survient, vérifier les informations entrées et que les fichiers de configuration soit bien placé dans `/opt/kactus/` sur l'hyperviseur suite au passage du script de primo-install (se référer au point 1.1.5 de cette documentation).
#### 1.2.5 - Stack `php_ip_am`
Dans l'onglet `build method`, cliquer sur `Repository`.
Rentrer les informations suivantes pour lier le repo Git à cette stack :
- Name : `php_ip_am`
- Repository URL : `https://github.com/Guillaume-Sanchez/kactus.git`
- Repository reference : `refs/heads/main`
- Compose path : `php_ip_am/docker-compose.yml`
- Activer `GitOps updates` et laisser sur `polling`
- Ajouter une variable d’environnement en cliquant sur `+ Add an environment variable` :
	-  MYSQL_ROOT_PASSWORD : `Mot_de_passe_root_de_la_BDD`

Pour finir, cliquer sur `Deploy the stcak`
> Si un problème survient, vérifier les informations entrées et que les fichiers de configuration soit bien placé dans `/opt/kactus/` sur l'hyperviseur suite au passage du script de primo-install (se référer au point 1.1.5 de cette documentation).
#### 1.2.6 - Stack `npm`
Dans l'onglet `build method`, cliquer sur `Repository`.
Rentrer les informations suivantes pour lier le repo Git à cette stack :
- Name : `npm`
- Repository URL : `https://github.com/Guillaume-Sanchez/kactus.git`
- Repository reference : `refs/heads/main`
- Compose path : `npm/docker-compose.yml`
- Activer `GitOps updates` et laisser sur `polling`

Pour finir, cliquer sur `Deploy the stcak`
> Si un problème survient, vérifier les informations entrées et que les fichiers de configuration soit bien placé dans `/opt/kactus/` sur l'hyperviseur suite au passage du script de primo-install (se référer au point 1.1.5 de cette documentation).
