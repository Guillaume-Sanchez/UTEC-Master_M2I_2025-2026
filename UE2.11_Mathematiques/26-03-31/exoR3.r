#Exo3 Simuler la somme des valeurs des faces obtenues en lançant 2 dés à 6 faces équilibrées
set.seed(123) # pour la reproductibilité
# Nombre de simulations
n <- 1000
# Simulation des deux dés
de1 <- sample(1:6, size = n, replace = TRUE)
de2 <- sample(1:6, size = n, replace = TRUE)
# Somme des deux dés
somme <- de1 + de2
# Affichage des premières valeurs pour vérifier
head(somme)
# Estimation de la fréquence de chaque somme possible (2 à 12)
table(somme) / n
# Histogramme des sommes
hist(somme,
     breaks = seq(1.5, 12.5, by = 1),
     col = "lightblue",
     main = "Histogramme des sommes de 2 dés",
     xlab = "Somme",
     ylab = "Fréquence")

