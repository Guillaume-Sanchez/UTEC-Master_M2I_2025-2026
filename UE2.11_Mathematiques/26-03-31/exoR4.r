# Exo4 Simuler la distribution du rang de la première boule rouge tirée, tirage AVEC remise Modèle d'urne : 
# Une urne contient m boules dont r rouges. On tire, successivement avec remise n boules dans l'urne et on note
# leurs couleurs dans l'ordre. La variable aléatoire X étudiée est le rang de la première rouge tirée
# (=0 si aucune rouge tirée au bout de n fois).
set.seed(123)
# Paramètres
m <- 10 # nombre total de boules
r <- 3 # nombre de boules rouges
n <- 5 # nombre de tirages
Nsim <- 10000 # nombre de simulations
# Probabilité de tirer une boule rouge à chaque tirage
p <- r / m
# Simulation
X <- numeric(Nsim)
for (i in 1:Nsim) {
tirages <- rbinom(n, size = 1, prob = p) # 1 = rouge, 0 = non rouge
if (any(tirages == 1)) {
X[i] <- which(tirages == 1)[1] # rang de la première rouge
} else {
X[i] <- 0
}
}
# Distribution empirique
distribution <- table(X) / Nsim
distribution
# Visualisation de la distribution
barplot(distribution,
col = "lightcoral",
main = "Distribution du rang de la première boule rouge",
xlab = "Rang de la première boule rouge (0 = aucune)",
ylab = "Probabilité")