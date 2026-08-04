### MATPLOTLIB
Matplotlib sert donc à :

transformer les données en graphiques ;
rendre les résultats plus faciles à comprendre ;
illustrer les conclusions de ton analyse.

C'est pour cette raison que pratiquement tous les rapports de Data Analyst contiennent des graphiques.

# Matplotlib

Matplotlib est une bibliothèque Python permettant de créer des graphiques afin de visualiser des données.

```python
import matplotlib.pyplot as plt
```

---

# Histogramme

## Principe

Un histogramme représente la répartition d'une variable numérique.

- Axe X : les valeurs de la variable.
- Axe Y : le nombre d'observations.

Il permet de répondre à des questions comme :

- Les données sont-elles réparties uniformément ?
- Où se concentrent les valeurs ?
- Existe-t-il des valeurs rares ou extrêmes ?

## Exemple

```python
plt.hist(df["mean radius"])
plt.show()
```

## Interprétation

Dans le dataset Breast Cancer Wisconsin :

- la majorité des tumeurs possèdent un rayon moyen compris entre 11 et 15 ;
- les très grands rayons sont beaucoup plus rares ;
- la distribution est asymétrique vers la droite.

## Personnaliser un graphique

### Titre

```python
plt.title("Titre")
```

Ajoute un titre au graphique.

---

### Axe X

```python
plt.xlabel("Nom de l'axe X")
```

Ajoute un nom à l'axe horizontal.

---

### Axe Y

```python
plt.ylabel("Nom de l'axe Y")
```

Ajoute un nom à l'axe vertical.

---

### Grille

```python
plt.grid()
```

Ajoute une grille afin de faciliter la lecture des valeurs.

# Diagramme en barres

## Principe

Un diagramme en barres permet de comparer des catégories.

Contrairement à un histogramme, il ne représente pas une variable numérique continue.

## Exemple

```python
diagnostic = df["diagnostic"].value_counts()

plt.bar(["Maligne", "Bénigne"], diagnostic.values)

plt.title("Répartition des diagnostics")

plt.xlabel("Diagnostic")

plt.ylabel("Nombre de patientes")

plt.grid(axis="y")

plt.show()
```

## Interprétation

Le dataset contient :

- 212 tumeurs malignes.
- 357 tumeurs bénignes.

Le jeu de données n'est donc pas parfaitement équilibré.

# Scatter Plot

## Principe

Un scatter plot (nuage de points) permet d'étudier la relation entre deux variables numériques.

Chaque point représente une observation du dataset.

- Axe X : première variable.
- Axe Y : seconde variable.

## Exemple

```python
plt.scatter(df["mean radius"], df["mean area"])

plt.title("Rayon moyen en fonction de la surface moyenne")

plt.xlabel("Rayon moyen")

plt.ylabel("Surface moyenne")

plt.grid()

plt.show()
```

## Interprétation

Le nuage de points montre une forte corrélation positive entre le rayon moyen et la surface moyenne.

Plus le rayon augmente, plus la surface augmente également.

# Légende

## label

Permet de donner un nom à une courbe ou à un graphique.

```python
label="Maligne"
```

---

## legend()

Affiche automatiquement la légende.

```python
plt.legend()
```

---

## alpha

Permet de rendre un graphique transparent.

```python
alpha=0.6
```

Très utile lorsque plusieurs graphiques sont affichés ensemble.

# Boxplot

## Principe

Un boxplot (ou boîte à moustaches) permet de comparer la distribution d'une variable entre plusieurs groupes.

Il résume rapidement les principales caractéristiques des données :

- la médiane ;
- la dispersion des valeurs ;
- les valeurs minimales et maximales normales ;
- les valeurs aberrantes (outliers).

Il est très utilisé en Data Analysis pour comparer deux populations.

---

## Exemple

```python
plt.boxplot([
    df[df["diagnostic"] == 0]["mean radius"],
    df[df["diagnostic"] == 1]["mean radius"]
])

plt.title("Rayon moyen selon le diagnostic")

plt.xticks([1, 2], ["Maligne", "Bénigne"])

plt.ylabel("Rayon moyen")

plt.grid()

plt.show()
```

---

## Lecture d'un boxplot

### La ligne au milieu de la boîte

Représente la **médiane**.

- 50 % des valeurs sont au-dessus.
- 50 % des valeurs sont en dessous.

---

### La boîte

Elle contient les **50 % des valeurs centrales**.

Une grande boîte indique une forte dispersion.

Une petite boîte indique que les valeurs sont plus homogènes.

---

### Les moustaches

Elles représentent les valeurs minimales et maximales considérées comme normales.

---

### Les points isolés

Les petits cercles représentent des **valeurs aberrantes** (*outliers*).

Ce sont des observations très éloignées de la majorité des données.

---

## Interprétation

Dans le dataset Breast Cancer Wisconsin :

- les tumeurs malignes possèdent généralement un rayon moyen plus élevé que les tumeurs bénignes ;
- la dispersion est plus importante chez les tumeurs malignes ;
- quelques patientes présentent des valeurs exceptionnellement élevées (outliers).

Le boxplot permet donc de comparer rapidement les distributions entre deux groupes sans calculer plusieurs statistiques séparément.