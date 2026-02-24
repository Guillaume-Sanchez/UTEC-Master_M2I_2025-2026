# Création des vecteurs pour les centres de classe et les effectifs
centres <- c(147.5, 152.5, 157.5, 162.5, 167.5, 172.5, 177.5, 182.5, 187.5, 192.5, 197.5, 202.5, 207.5)
effectifs <- c(2, 2, 5, 14, 38, 52, 76, 50, 40, 13, 5, 2, 1)

# Calcul du nombre total de jours (doit être égal à 300 selon l'énoncé)
N <- sum(effectifs)

# Calcul des fréquences
frequences <- effectifs / N

# Arrondi à 3 chiffres après la virgule comme demandé
frequences_arrondies <- round(frequences, 3)

# Pour afficher le résultat dans la console
print(frequences_arrondies)

# Calcul de la moyenne pondérée
moyenne <- sum(centres * effectifs) / N
cat("La moyenne est de :", moyenne, "K€\n")

# Calcul de la variance
variance <- sum(effectifs * (centres - moyenne)^2) / N

# Calcul de l'écart-type (racine carrée de la variance)
ecart_type <- sqrt(variance)
cat("L'écart-type est de :", ecart_type, "K€\n")

# Création du graphique (type = "b" signifie "both" : points et lignes)
plot(centres, effectifs, 
     type = "b", 
     pch = 19,               # Forme des points (ronds pleins)
     col = "darkblue",       # Couleur de la ligne et des points
     lwd = 2,                # Épaisseur de la ligne
     main = "Profil des ventes au cours de l'année", # Titre
     xlab = "Chiffre d'affaires (K€)",               # Titre de l'axe X
     ylab = "Nombre de jours")                       # Titre de l'axe Y

# Optionnel : ajouter une grille pour faciliter la lecture
grid()