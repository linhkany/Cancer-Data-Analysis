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

# Scikit-learn

## Import

```python
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
```

---

## Charger un dataset

```python
cancer = load_breast_cancer()
```

---

## Créer un DataFrame

```python
df = pd.DataFrame(cancer.data, columns=cancer.feature_names)
df["diagnostic"] = cancer.target
```

---

## Variables explicatives (Features)

```python
X = df.drop("diagnostic", axis=1)
```

---

## Variable cible (Target)

```python
y = df["diagnostic"]
```

---

## Séparer les données

```python
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
```

---

## Standardiser les données

```python
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
```

---

## Créer un modèle

```python
model = LogisticRegression()
```

---

## Entraîner le modèle

```python
model.fit(X_train, y_train)
```

---

## Faire des prédictions

```python
y_pred = model.predict(X_test)
```

---

## Accuracy

```python
accuracy = accuracy_score(y_test, y_pred)
```

---

## Matrice de confusion

```python
confusion_matrix(y_test, y_pred)
```

---

## Classification Report

```python
classification_report(y_test, y_pred)
```