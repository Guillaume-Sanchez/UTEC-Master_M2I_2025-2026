# 24 02 26

💡 Qu'est-ce que la loi de Poisson ?

La loi de Poisson sert à modéliser le nombre de fois qu'un événement se produit dans un intervalle de temps (ou d'espace) donné, lorsque l'on connaît la fréquence moyenne de cet événement.

Pour l'utiliser, il faut que :

- Les événements soient indépendants (une panne n'en entraîne pas une autre).
- Les événements se produisent de manière aléatoire.
- On connaisse le nombre moyen d'apparitions sur la période (le fameux paramètre λ, prononcé "lambda").

La formule magique :
Pour calculer la probabilité que l'événement se produise exactement k fois, on utilise cette formule :
```
P(X=k)=k!e−λ⋅λk​
```
- **X** : C'est ce qu'on cherche (le nombre de pannes).
- **k** : Le nombre exact de pannes pour lequel on veut calculer la probabilité (0, 1, 2, 3...).
- **λ (lambda)** : La moyenne habituelle de pannes sur la période.
- **e** : La constante mathématique exponentielle (environ 2,718).
- **k!** (factorielle de k) : C'est la multiplication de tous les entiers de 1 à k (ex: 4!=4×3×2×1=24). Note : 0! est toujours égal à 1.

## Application 2 – Les pannes de machine

### 1- Calculer le paramètre de la loi de Poisson suivie par X.

Le paramètre d'une loi de Poisson est noté λ. Il représente la moyenne des événements sur la période étudiée.
Dans le texte, il est écrit : "au cours d'une période de 8 heures de travail, le nombre moyen de pannes [...] était de 4".

`Réponse : Le paramètre de la loi de Poisson est λ = 4.`

### 2- Calculer l’espérance mathématique, la variance et l’écart-type.

L'Espérance E(X) : C'est la moyenne attendue. Pour une loi de Poisson, l'espérance est toujours égale au paramètre λ.
```
E(X)=λ=4 (Cela signifie qu'en moyenne, on s'attend à 4 pannes).
```

La Variance V(X) : Fait remarquable de la loi de Poisson, la variance (qui mesure la dispersion autour de la moyenne) est aussi égale à λ.
```
V(X)=λ=4
```
L'Écart-type σ(X) : C'est toujours la racine carrée de la variance.
```
σ(X)=V(X)​=4​=2 (Cela signifie que le nombre de pannes s'écarte en moyenne de 2 pannes par rapport à l'espérance de 4).
```
### 3- Calculer les probabilités

Notre formule de base pour cet exercice est donc : 
P(X=k)=k!e−4⋅4k​

- a. Égal à 2 pannes (P(X=2)) :
```
Ici, k=2.
P(X=2)=2!e−4⋅42​
P(X=2)=2×10,0183⋅16​
P(X=2)=20,2928​≈0,1465
```
`Réponse : Il y a environ 14,65 % de chances d'avoir exactement 2 pannes.`

- b. Égal à 4 pannes (P(X=4)) :
```
Ici, k=4.
P(X=4)=4!e−4⋅44​
P(X=4)=4×3×2×10,0183⋅256​
P(X=4)=244,6848​≈0,1954
```

`Réponse : Il y a environ 19,54 % de chances d'avoir exactement 4 pannes. (C'est la probabilité la plus élevée, ce qui est logique puisque 4 est la moyenne !).`

- c. Inférieur ou égal à 4 pannes (P(X≤4)) :
Ici, il faut additionner les probabilités d'avoir 0, 1, 2, 3 et 4 pannes.
```
P(X≤4)=P(X=0)+P(X=1)+P(X=2)+P(X=3)+P(X=4)

    P(X=0)=0!e−4⋅40​≈0,0183

    P(X=1)=1!e−4⋅41​≈0,0733

    P(X=2)≈0,1465 (calculé en a)

    P(X=3)=3!e−4⋅43​≈0,1954

    P(X=4)≈0,1954 (calculé en b)

Total : 0,0183+0,0733+0,1465+0,1954+0,1954=0,6289
```
`Réponse : Il y a environ 62,89 % de chances d'avoir 4 pannes ou moins.`

- d. Strictement supérieur à 4 pannes (P(X>4)) :

Plutôt que de calculer P(X=5)+P(X=6)+P(X=7)... jusqu'à l'infini (ce qui est impossible), on utilise l'astuce de l'événement contraire.

La somme de toutes les probabilités est toujours égale à 1 (soit 100%).

Donc : Probabilité(plus de 4 pannes) = 1 - Probabilité(4 pannes ou moins).
```
P(X>4)=1−P(X≤4)
P(X>4)=1−0,6289=0,3711
```
`Réponse : Il y a environ 37,11 % de chances d'avoir strictement plus de 4 pannes.`