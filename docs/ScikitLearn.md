# Scikit-Learn

## Import

from sklearn.datasets import load_breast_cancer

Importer le jeu de données Breast Cancer.

## Charger le dataset

load_breast_cancer()

Charger le jeu de données.

## Variables explicatives

X = df.drop("diagnostic", axis=1)

Créer les variables d'entrée.

## Variable cible

y = df["diagnostic"]

Créer la variable cible.

## Séparer les données

train_test_split()

Séparer les données d'entraînement et de test.

## Import

from sklearn.model_selection import train_test_split

Importer la fonction.

## Modèle

LogisticRegression()

Créer un modèle de régression logistique.

## Import

from sklearn.linear_model import LogisticRegression

Importer le modèle.

## Entraîner le modèle

model.fit(X_train, y_train)

Entraîner le modèle.

## Faire des prédictions

model.predict(X_test)

Prédire les résultats.

## Probabilités

model.predict_proba(X_test)

Retourner les probabilités.

## Précision

accuracy_score()

Calculer la précision du modèle.

## Import

from sklearn.metrics import accuracy_score

Importer la fonction.

## Matrice de confusion

confusion_matrix()

Afficher les prédictions correctes et incorrectes.

## Import

from sklearn.metrics import confusion_matrix

Importer la fonction.

## Rapport de classification

classification_report()

Afficher les métriques du modèle.

## Import

from sklearn.metrics import classification_report

Importer la fonction.

## Sauvegarder un modèle

joblib.dump(model, "model.pkl")

Sauvegarder un modèle entraîné.

## Charger un modèle

joblib.load("model.pkl")

Charger un modèle sauvegardé.