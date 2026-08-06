from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import pandas as pd

# Chargement du dataset
cancer = load_breast_cancer()

# Création du DataFrame
df =  pd.DataFrame(cancer.data, columns=cancer.feature_names)

# Ajout de la cible
df["diagnostic"] = cancer.target

# Variables explicatives (features)
x = df.drop("diagnostic", axis = 1)

# Variable cible (target)
y = df["diagnostic"]

print(x.head())
print()
print(y.head())

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42 ) # test_size = 0.2 signifie 20% de données serviront au test.
# random_state = 42 => découpage au hasard
print("x_train:", x_train.shape)
print("x_test:", x_test.shape)
print()
print("y_train:", y_train.shape)
print("y_test:", y_test.shape)

from sklearn.preprocessing import StandardScaler
# Création du scaler
scaler = StandardScaler()
# Apprentissage sur les données d'entraînement
x_train = scaler.fit_transform(x_train)

# Transformation des données de test
x_test = scaler.transform(x_test)
print(x_train[:5])

# Création du modèle
model = LogisticRegression()
model.fit(x_train, y_train)
print("Le modèle a été entraîné avec succès!")

# modèle apprise donc on va faire des prédictions.
y_pred = model.predict(x_test)
print("Prédictions: ")
print(y_pred[:10])
print()
print("Vraies valeurs: ")
print(y_test.values[:10])

accuracy = accuracy_score(y_test, y_pred) # mesurer à quel point cette règle est bonne
print("Accuracy:", accuracy)
print(f"Accuracy: {accuracy * 100:.2f}%")

# MATRICE DE CONFUSION: voir quelles erreurs le modèle fait réellement 
cm = confusion_matrix(y_test, y_pred)
print(cm)

# CLASSIFICATION REPORT: donne le rapport complet
print(classification_report(y_test, y_pred))
