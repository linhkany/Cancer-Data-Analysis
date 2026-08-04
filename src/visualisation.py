# Contient uniquement le code Matplotlib
import matplotlib.pyplot as plt

#plt.plot([1, 2, 3, 4], [10, 15, 8, 20])
#plt.show()

from sklearn.datasets import load_breast_cancer
import pandas as pd 
import matplotlib.pyplot as plt 

# Chargement des données 
cancer = load_breast_cancer()

df = pd.DataFrame(cancer.data, columns=cancer.feature_names)
df["diagnostic"] = cancer.target

# Histogramme
plt.hist(df["mean radius"])

plt.title("Distribution du rayon moyen des tumeurs")

plt.xlabel("Rayon moyen")

plt.ylabel("Nombre de patientes")

plt.grid()

plt.show()

# Histogramme de "mean area"
plt.hist(df["mean area"], color = "skyblue", bins = 20, edgecolor = "blue"  )
plt.title("Distribution de la surface moyenne des tumeurs")
plt.xlabel("Surface moyenne")
plt.ylabel("Nombre de patientes")

plt.grid()
plt.show()


diagnostic = df["diagnostic"].value_counts()
plt.bar(["Maligne", "Bénigne"], [diagnostic[0], diagnostic[1]], color = "pink")
plt.title("Répartition des diagnostics")
plt.xlabel("Diagnostic")
plt.ylabel("Nombre de patientes")
plt.grid(axis="y")
plt.show()

plt.scatter(df["mean radius"], df["mean area"])
plt.title("Rayon moyen en fonction de la surface moyenne")
plt.xlabel("Rayon moyen")
plt.ylabel("Surface moyenne")
plt.grid()
plt.show()

plt.boxplot([df[df["diagnostic"] == 0]["mean radius"], df[df["diagnostic"] == 1]["mean radius"]])
plt.title("Rayon moyen selon le diagnostic")
plt.xticks([1, 2], ["Maligne", "Bénigne"])
plt.ylabel("Rayon moyen")
plt.grid()
plt.show()

plt.hist(df[df["diagnostic"] == 0]["mean radius"], bins=20, alpha=0.6, label="Maligne", color = "green")
plt.hist(df[df["diagnostic"] == 1]["mean radius"], bins=20, alpha=0.6, label="Bénigne", color = "pink")
plt.title("Distribution du rayon moyen selon le diagnostic")
plt.xlabel("Rayon moyen")
plt.ylabel("Nombre de patientes")
plt.legend()
plt.grid()
plt.show()


