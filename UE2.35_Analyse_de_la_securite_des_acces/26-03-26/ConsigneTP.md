# Devoir : Mise en œuvre d'une PKI et sécurisation de flux critiques avec OpenSSL
## Contexte
L'entreprise CyberSafe Corp souhaite mettre en place une infrastructure de gestion de clés (PKI) interne pour sécuriser les échanges de rapports d'audit entre ses consultants (Alice) et ses administrateurs (Bob).
Vous êtes chargé de simuler cette infrastructure et de réaliser un transfert sécurisé en respectant des contraintes cryptographiques strictes.
Objectifs pédagogiques
- Mettre en place une Autorité de Certification (AC) racine.
- Comprendre le cycle de vie d'un certificat (Clé → CSR → Certificat).
- Maîtriser le chiffrement hybride pour contourner les limites du chiffrement asymétrique.
- Garantir l'intégrité et la non-répudiation via la signature numérique.

## Travail à réaliser
### Partie 1 : Déploiement de l'Infrastructure de Confiance (PKI)

Autorité Racine :

- Générez une clé privée RSA de 2048 bits pour l'AC.
- Utilisez un exposant public de 3.
- Générez ensuite un certificat racine auto-signé (CA.crt) d'une validité de 10 ans.

Entités Finales :

- Générez les couples de clés pour Alice et Bob.

Certification :

- Créez une demande de signature (CSR) pour Alice et Bob.
- Signez ces demandes avec la clé de l'AC pour produire les certificats finaux (alice.crt et bob.crt).

Vérification :

- Prouvez mathématiquement que le certificat de Bob est bien issu de votre AC via une commande OpenSSL.

### Partie 2 : Préparation du transfert sécurisé (Alice)

- Alice doit envoyer un fichier rapport_audit.pdf de 15 Mo à Bob.

Génération de session :

- Générez une clé symétrique de 256 bits au format Base64.

Confidentialité :

- Chiffrez le rapport avec l'algorithme AES-256-CBC.
- Vous devez impérativement utiliser pbkdf2 avec au moins 100 000 itérations pour la dérivation de clé.

Transport de clé :

- Utilisez la clé publique de Bob pour chiffrer la clé de session.

Authentification :

- Produisez une signature numérique de la clé de session en utilisant la clé privée d'Alice et l'algorithme SHA-256.

### Partie 3 : Réception et Audit (Bob)

- Simulez la réception des fichiers par Bob dans un répertoire séparé.

Extraction :

- Extrayez la clé publique d'Alice de son certificat.

Vérification de l'origine :

- Vérifiez la signature de la clé de session.
- Expliquez ce que Bob conclurait si cette étape échouait.

Accès aux données :

- Déchiffrez la clé de session, puis le rapport d'audit.

## Livrables attendus

### Rapport technique (PDF) :

- Capture d'écran de la commande prouvant la validité de la chaîne de confiance.
- Explication technique : Pourquoi ne peut-on pas chiffrer directement le rapport de 15 Mo avec la clé publique de Bob ?
- Analyse de sécurité : Quel est l'impact de l'utilisation de l'exposant e=3 par rapport au standard e=65537 ?
- Preuve d'intégrité : Fournissez les empreintes SHA-256 du fichier original et du fichier final déchiffré.

### Barème de notation

- Infrastructure (5 pts) : Configuration correcte de l'AC et des certificats.
- Chiffrement Hybride (5 pts) : Utilisation correcte d'AES et transport de la clé via RSA.
- Signature (4 pts) : Mise en œuvre de la non-répudiation.
- Analyse (4 pts) : Qualité des explications sur les limites de RSA et le rôle du padding/PBKDF2.
- Rigueur (2 pts) : Comparaison des sommes de contrôle (checksums).
