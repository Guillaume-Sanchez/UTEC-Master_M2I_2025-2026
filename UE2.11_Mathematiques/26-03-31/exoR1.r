# Exo1 Exemple de 1000 simulations du jet d'une pièce équilibrée pour estimer la probabilité d'obtenir "pile"
set.seed(123)
# Simulation de 1000 jets (0 = face, 1 = pile)
jets <- rbinom(1000, 1, 0.5)
# Histogramme
hist(jets,
  breaks = c(-0.5, 0.5, 1.5),
  main = "Histogramme des résultats des jets",
  xlab = "Résultat",
  ylab = "Fréquence",
  col = "lightblue",
  xaxt = "n")
  axis(1, at = c(0, 1), labels = c("Face", "Pile"))