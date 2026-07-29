# Pandas

## Import

import pandas as pd

Importer Pandas.

## DataFrame

df = pd.DataFrame(data)

Créer un DataFrame.

## Premières lignes

df.head()

Afficher les 5 premières lignes.

## Dernières lignes

df.tail()

Afficher les 5 dernières lignes.

## Dimensions

df.shape

Retourner (lignes, colonnes).

## Colonnes

df.columns

Afficher le nom des colonnes.

## Informations

df.info()

Afficher les informations du DataFrame.

## Statistiques

df.describe()

Afficher :
- count
- mean
- std
- min
- 25%
- 50%
- 75%
- max

## Sélectionner une colonne

df["colonne"]

Retourner une Series.

## Moyenne

df["colonne"].mean()

Calculer la moyenne.

## Minimum

df["colonne"].min()

Retourner la plus petite valeur.

## Maximum

df["colonne"].max()

Retourner la plus grande valeur.

## Somme

df["colonne"].sum()

Calculer la somme.

## Médiane

df["colonne"].median()

Calculer la médiane.

## Écart-type

df["colonne"].std()

Calculer l'écart-type.

## Valeurs uniques

df["colonne"].unique()

Afficher les valeurs uniques.

## Occurrences

df["colonne"].value_counts()

Compter les occurrences.

## Filtrer

df[df["colonne"] > valeur]

Filtrer les lignes.

## Trier

df.sort_values("colonne")

Trier le DataFrame.

## Lire un CSV

df = pd.read_csv("patients.csv")

Lire un fichier CSV.

## Sauvegarder un CSV

df.to_csv("patients.csv", index=False)

Sauvegarder un DataFrame.

## loc et iloc

Affiche les lignes d'une colonne

Quand utiliser lequel ?

En pratique :

✅ loc : quand tu connais le nom des colonnes ("mean radius", "target", etc.). C'est le plus courant en analyse de données.
✅ iloc : quand tu veux les n premières colonnes, la 5ᵉ ligne, ou quand tu ne veux pas écrire les noms des colonnes.

df.loc[:, "Ville"]
df.iloc[:, 2]

## Manipulation et filtrage des données

## Sélection d'une colonne

```python
df["mean radius"]
```

Retourne une colonne (Series).

---

## Sélection de plusieurs colonnes

```python
df[["mean radius", "mean texture"]]
```

Retourne un DataFrame contenant uniquement les colonnes sélectionnées.

---

## Différence entre Series et DataFrame

### Series

Une seule colonne.

```python
df["mean radius"]
```

### DataFrame

Une ou plusieurs colonnes.

```python
df[["mean radius", "mean texture"]]
```

---

## loc

Sélection par **nom** des lignes et des colonnes.

```python
df.loc[0]
```

Première ligne.

```python
df.loc[0:4]
```

Lignes 0 à 4 (4 inclus).

```python
df.loc[0:4, ["mean radius", "diagnostic"]]
```

Lignes 0 à 4 avec uniquement les colonnes sélectionnées.

---

## iloc

Sélection par **position**.

```python
df.iloc[0]
```

Première ligne.

```python
df.iloc[0:5]
```

Les 5 premières lignes.

```python
df.iloc[0:5, 0:3]
```

Les 5 premières lignes et les 3 premières colonnes.

---

## Filtrer des données

### Égal

```python
df[df["diagnostic"] == 0]
```

---

### Différent

```python
df[df["diagnostic"] != 0]
```

---

### Supérieur

```python
df[df["mean radius"] > 20]
```

---

### Inférieur

```python
df[df["mean texture"] < 15]
```

---

### Supérieur ou égal

```python
df[df["mean area"] >= 1000]
```

---

## Plusieurs conditions (ET)

Toutes les conditions doivent être vraies.

```python
df[(df["mean radius"] > 18) & (df["mean texture"] > 20)]
```

---

## Plusieurs conditions (OU)

Au moins une condition doit être vraie.

```python
df[(df["diagnostic"] == 0) | (df["mean radius"] > 25)]
```

---

## Trier les données

### Ordre croissant

```python
df.sort_values(by="mean radius")
```

---

### Ordre décroissant

```python
df.sort_values(by="mean radius", ascending=False)
```

---

## Chaîner plusieurs commandes

Exemple :

```python
df[df["diagnostic"] == 0].sort_values(by="mean area", ascending=False)
```

Filtre les tumeurs malignes puis les trie par surface décroissante.

---

## À retenir

- `[]` : sélectionner des colonnes.
- `loc` : sélection par nom.
- `iloc` : sélection par position.
- `==`, `!=`, `>`, `<`, `>=`, `<=` : filtrer.
- `&` : ET.
- `|` : OU.
- `sort_values()` : trier les données.
- `ascending=False` : tri décroissant.
- Les conditions multiples doivent toujours être entourées de parenthèses.