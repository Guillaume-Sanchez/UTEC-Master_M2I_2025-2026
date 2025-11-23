# Documentation technique Guillaume Sanchez

Mise en place d'un environement docker des services de l'entreprise Kactus

> Cette Documentation est vable sur un machine sous la disctribution Debian 13

## Installation de Docker

### Installez le Référentiel `apt` de Docker.

```
# Add Docker's official GPG key:
sudo apt update
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

### Installez les paquets Docker

```
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

### Vérifiez que l'installation est réussie en exécutant le `hello-world` image

```
sudo docker run hello-world
```

### Gestion du service Docker

Pour vérifier le status des services docker :

```
sudo systemctl status docker
```

Pour démarrer les services docker :

```
sudo systemctl start docker
```

Pour stopper les services docker :

```
sudo systemctl stop docker
```

Pour redémarrer les services docker :

```
sudo systemctl restart docker
```

Pour désactiver le lancement des services docker au démarrage de la :

```
sudo systemctl disable docker
```

Pour activer le lancement des services docker au démarrage de la :

```
sudo systemctl enable docker
```

## Installation de Portainer

### Prérequis

Avoir Docker

### Installez Portainer avec Docker.

Pour installer Portainer, exécutez les commandes suivante :

```
docker volume create portainer_data
docker run -d -p 9000:9000 --name=portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce
```

Voici ce que cette commande fait :

- Crée un volume Docker portainer_data pour stocker les données de Portainer de manière persistante.
- Démarre un nouveau conteneur Docker nommé portainer qui exécute Portainer, configuré pour redémarrer automatiquement.
- Expose le port 9000, sur lequel l’interface utilisateur web de Portainer sera accessible.
- Montre le socket Docker dans le conteneur, permettant à Portainer de gérer les conteneurs sur l’hôte Docker.

### Accèder au portail Portainer

Une fois Portainer lancé, vous pouvez accéder à l’interface utilisateur :
 
[http://votre_adresse_ip_serveur:9000](http://localhost:9000)

Sur la page d’accueil de Portainer, vous serez invité à créer un utilisateur administrateur. Remplissez les détails demandés et connectez-vous

## Installation de Wordpress et de sa BDD

### Prérequis

### Installation avec Docker-composer

```yaml
version: '2'

services:
   db:
     image: mariadb
     volumes:
       - db_data:/var/lib/mysql
     restart: always
     environment:
       MYSQL_ROOT_PASSWORD: ${MYSQL_DATABASE_PASSWORD}
       MYSQL_DATABASE: wordpress
       MYSQL_USER: wordpress
       MYSQL_PASSWORD: wordpress

   wordpress:
     image: wordpress:latest
     ports:
       - 80
     restart: always
     environment:
       WORDPRESS_DB_HOST: db:3306
       WORDPRESS_DB_USER: wordpress
       WORDPRESS_DB_PASSWORD: wordpress

volumes:
    db_data:
```
