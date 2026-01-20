# 26 01 20

## Instalation de R studio sur Linux :

```
sudo apt update
sudo apt install r-base r-base-dev
```

Puis [Télécharger r studio desktop](https://posit.co/download/rstudio-desktop/)

```
cd ~/Téléchargements
sudo apt install ./rstudio-*.deb
```

## 1.1

> ∪ ou

> ∩ et / inter

Si on prend un jeu de 32 cartes :

on veut un valet, on a 4/32 donc 1/8 chance de l'avoir
on veut une carte de couleur pique, on a 8/32 donc 1/4 chance d'en avoir.
on veut un valet de pique, on a 1/32 de l'avoir

Si on veut un valet ou un pique, on a P(pique) + P(valet) - P(piquedeValet)
Donc on a 1/8 + 1/4 - 1/32
Donc 4 + 8 - 1 / 32 Donc 11/32 chance d'avoir ou un valet ou du pique

P(A ∪ B) = P(A) + P(B) - P(A ∩ B)

