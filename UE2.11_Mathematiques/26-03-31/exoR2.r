# Exo2 Exemple de 1000 simulations du jet d'un dé à 6 faces équilibrées pour estimer la probabilité d'obtenir laface "4".
set.seed(123) # pour que les résultats soient reproductibles
# Nombre de simulations
n <- 1000
# Simulation des lancers (1 à 6)
jets <- sample(1:6, size = n, replace = TRUE)
# Estimation de la probabilité d'obtenir un "4"
prob_4 <- mean(jets == 4)
# Affichage du résultat
cat("Probabilité estimée d'obtenir la face 4 :", prob_4, "\n")
# Histogramme des résultats
hist(jets,
     breaks = 0.5:6.5, # pour centrer les barres sur les faces
     col = "lightgreen",
     main = "Histogramme des lancers de dé",
     xlab = "Face du dé",
     ylab = "Fréquence")
