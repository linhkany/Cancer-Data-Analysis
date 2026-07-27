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