from sklearn.datasets import load_breast_cancer
import pandas as pd

cancer = load_breast_cancer()

df = pd.DataFrame(cancer.data, columns = cancer.feature_names)
df["diagnostic"] = cancer.target

# JOUR 7
# Mission - Première analyse statistique

# Tu travailles dans un laboratoire qui étudie le cancer du sein. Le responsable veut un premier rapport statistiques avant de construire un modèle de Machine Learning.

# Question 1: Combien y a - t - il de patientes?
print(df.shape) # (569, 31) il y a 569 patientes au total dont 31 colonnes de caractéristiques différentes.
print(df["diagnostic"].value_counts()) # 1    357; 0    212 => il y a 357 patientes atteintes d'une tumeur bénigne et 212 patientes atteintes d'une tumeur maligne.

# Question 2: 
print(df.columns)
print(df.groupby("diagnostic")[["mean radius", "mean texture", "mean area"]].mean())

# Question 3:
print(df.groupby("diagnostic")["mean radius"].agg(["mean", "median", "min", "max", "std"]))

# Question 4:
print(df[(df["diagnostic"] == 0) & (df["mean area"] > 900)])

# Question 5: 
print(df[(df["diagnostic"] == 0) | (df["mean radius"] > 25)][["mean radius", "mean texture", "mean area", "diagnostic"]].sort_values( by = "mean radius", ascending=False))