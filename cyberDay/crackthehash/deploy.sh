#!/bin/bash

# 1. Créer un dossier pour le projet
mkdir -p crackthehash
cd crackthehash

echo "--- Génération du fichier docker-compose.yml ---"

# 2. Générer le docker-compose via EOF
cat <<EOF > docker-compose.yml
services:
  web:
    image: php:8.2-apache
    container_name: crackthehash
    restart: always
    ports:
      - "8081:80"
    volumes:
      - ./html:/var/www/html
      - ./my-httpd.conf:/etc/apache2/sites-enabled/000-default.conf
EOF

echo "--- Génération de la configuration Apache ---"

# 3. Générer la config Apache via EOF
cat <<EOF > my-httpd.conf
<VirtualHost *:80>
    DocumentRoot /var/www/html
    <Directory /var/www/html>
        AllowOverride All
        Require all granted
    </Directory>
    ErrorLog \${APACHE_LOG_DIR}/error.log
    CustomLog \${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
EOF

echo "--- Récupération du site web ---"

# 4. Cloner ou télécharger les fichiers du site
mkdir -p html
git clone https://github.com/Guillaume-Sanchez/UTEC-Master_M2I_2025-2026.git
mv UTEC-Master_M2I_2025-2026/cyberDay/crackthehash/dev/build/* html/
rm -rf UTEC-Master_M2I_2025-2026

echo "--- Lancement des conteneurs ---"

# 5. Lancer Docker
docker compose up -d

echo "✅ Déploiement terminé ! Site accessible sur http://localhost/:8081"
