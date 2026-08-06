# 🧬 Cancer Data Analysis

Mon premier mini projet de Data Science.

Objectif :
Utilisation du Python, analyser un dataset sur le cancer et construire un modèle de prédiction.
(Rappel du langage Python, renforcement des bases)
Durée donnée: 1 mois ou moins, en mode chill.

À la fin du projet, je serai capable de :

- Charger un jeu de données médical.
- Explorer et analyser les données.
- Réaliser des visualisations pertinentes.
- Construire un premier modèle de Machine Learning.
- Présenter un projet professionnel sur GitHub.

## 🚀 Progression

### ✅ Jour 1
- Installation de Python
- Installation de VS Code
- Installation de Git
- Création du projet
- Premier programme Python

### ✅ Jour 2
- Variables
- Types de données (`int`, `float`, `str`, `bool`)
- `print()`
- `input()`
- Opérations mathématiques
- Calcul de l'IMC
- Conditions (`if`, `elif`, `else`)

### Difficultés rencontrées

- Rappel de pourquoi `input()` renvoie du texte.
- Rappel du rôle de `float()`.
- Rappel de pourquoi on écrit :

```python
age = age + 1
```

- Comprendre quand utiliser `round()`.

### Résultat

J'ai réalisé mon premier petit programme interactif capable de :

- demander la taille et le poids de l'utilisateur ;
- calculer son IMC ;
- afficher la catégorie correspondante.

### ✅ Jour 3
- Listes Python
- Boucles `for`
- Dictionnaires
- Listes de dictionnaires
- Manipulation d'une petite base de données de patients
- Parcours et affichage des informations des patients

### ✅ Jour 4 : Fonctions et organisation du projet
- Création de fonctions avec `def`
- Paramètres
- Utilisation de `return`
- Fonctions retournant des nombres, des booléens, des listes et des dictionnaires
- Import de modules Python
- Organisation du projet en plusieurs fichiers

**Exercices réalisés :**
- Affichage des informations d'un patient
- Calcul de l'âge moyen des patients
- Comptage des patients atteints d'un diagnostic malin
- Recherche du patient le plus âgé
- Filtrage des patients selon un critère (diagnostic, âge...)

**Organisation du projet :**
- Création du fichier `patients.py`
- Séparation des fonctions et du programme principal (`main.py`)
- Utilisation de `from patients import *`

**Git & GitHub :**
- Configuration de Git (`user.name` et `user.email`)
- Création du premier commit
- Création du dépôt GitHub
- Premier `git push`
- Mise en place d'un fichier `.gitignore`

### ✅ Jour 5 : Pandas - Premières analyses de données

- Installation de Pandas
- Découverte du DataFrame
- Chargement du dataset Breast Cancer
- Exploration des données
- Statistiques descriptives
- Manipulation des colonnes
- Filtrage des données
- Tri des données

**Commandes étudiées :**

- `head()`
- `tail()`
- `shape`
- `columns`
- `info()`
- `describe()`
- `mean()`
- `median()`
- `std()`
- `min()`
- `max()`
- `sum()`
- `unique()`
- `value_counts()`
- `sort_values()`
- Filtrage avec des conditions

**Documentation réalisée :**

- Création de `Python.md`
- Création de `Pandas.md`
- Création de `ScikitLearn.md`
- Création de `SQL.md`
- Création de `Concepts.md`
- Création de `Ressources.md`

**Projet :**

- Organisation du dossier `docs`
- Amélioration de la structure du projet
- Mise à jour du dépôt GitHub

**Compétences acquises :**

✅ Manipuler un DataFrame

✅ Explorer un jeu de données

✅ Calculer des statistiques descriptives

✅ Filtrer et trier les données

✅ Documenter un projet Python

## 📅 Jour 6 – Manipulation et filtrage des données avec Pandas

### 🎯 Objectifs
- Comprendre la différence entre une **Series** et un **DataFrame**.
- Sélectionner des lignes et des colonnes.
- Filtrer les données selon une ou plusieurs conditions.
- Trier les résultats.
- Manipuler les données comme un Data Analyst.

### 📚 Notions étudiées
- `loc[]`
- `iloc[]`
- Sélection d'une ou plusieurs colonnes
- Filtrage avec :
  - `==`
  - `!=`
  - `>`
  - `<`
  - `>=`
  - `<=`
- Combinaison de conditions avec :
  - `&` (ET)
  - `|` (OU)
- `sort_values()`
- Tri par ordre croissant et décroissant (`ascending=True` / `ascending=False`)
- Chaînage de plusieurs commandes Pandas

### 💻 Exercices réalisés
- Affichage d'une ou plusieurs colonnes d'un DataFrame.
- Sélection de lignes avec `loc` et `iloc`.
- Filtrage des tumeurs bénignes et malignes.
- Utilisation de plusieurs conditions avec les opérateurs `&` et `|`.
- Tri des données selon différentes caractéristiques (`mean radius`, `mean area`...).
- Résolution d'une mission simulant une demande d'un médecin pour identifier des patientes répondant à des critères précis.

### ✅ Compétences acquises
À la fin de cette journée, je suis capable de :
- Comprendre la différence entre une **Series** et un **DataFrame**.
- Sélectionner efficacement des lignes et des colonnes.
- Filtrer un jeu de données avec des conditions simples ou multiples.
- Trier les données afin de faciliter leur analyse.
- Enchaîner plusieurs opérations Pandas dans une même commande.
- Traduire une problématique métier en requête Pandas.

---

## 📅 Jour 7 – Analyse statistique avec Pandas

### 🎯 Objectifs
- Comprendre le principe de `groupby()`.
- Calculer des statistiques descriptives.
- Comparer les tumeurs bénignes et malignes.
- Commencer à interpréter les résultats.
- Répondre à des problématiques de Data Analyst.

### 📚 Notions étudiées
- `groupby()`
- `count()`
- `value_counts()`
- `mean()`
- `median()`
- `min()`
- `max()`
- `std()`
- `agg()`
- Analyse statistique par groupe
- Interprétation des résultats

### 💻 Exercices réalisés
- Comptage du nombre de patientes par diagnostic.
- Calcul des moyennes de plusieurs caractéristiques par diagnostic.
- Comparaison des rayons, textures et surfaces moyennes.
- Utilisation de `agg()` pour obtenir plusieurs statistiques en une seule commande.
- Recherche des patientes répondant à différents critères médicaux.
- Première mission d'analyse simulant une étude réalisée pour un laboratoire.

### ✅ Compétences acquises
À la fin de cette journée, je suis capable de :
- Regrouper des données avec `groupby()`.
- Calculer des statistiques descriptives.
- Comparer plusieurs groupes de données.
- Utiliser `agg()` pour résumer efficacement un dataset.
- Interpréter les résultats d'une analyse statistique.
- Répondre à des questions métier à partir des données.

## 📅 Jour 8 – Visualisation des données avec Matplotlib

### 🎯 Objectifs
- Découvrir Matplotlib.
- Comprendre les principaux types de graphiques.
- Visualiser les données du dataset Breast Cancer Wisconsin.
- Interpréter les graphiques comme un Data Analyst.

### 📚 Notions étudiées
- `plt.hist()`
- `plt.bar()`
- `plt.scatter()`
- `plt.boxplot()`
- `plt.title()`
- `plt.xlabel()`
- `plt.ylabel()`
- `plt.grid()`
- `plt.legend()`
- `plt.xticks()`
- `plt.savefig()`
- `alpha`
- `bins`
- `edgecolor`

### 📊 Graphiques réalisés
- Histogramme du rayon moyen
- Histogramme de la surface moyenne
- Diagramme en barres des diagnostics
- Scatter plot : rayon moyen vs surface moyenne
- Boxplot : comparaison du rayon moyen selon le diagnostic

### 💻 Compétences acquises
À la fin de cette journée, je suis capable de :
- Choisir le graphique adapté à une question d'analyse.
- Personnaliser un graphique avec un titre, des axes et une grille.
- Comparer deux groupes à l'aide d'un boxplot.
- Étudier la relation entre deux variables grâce à un scatter plot.
- Sauvegarder des graphiques pour les intégrer dans un rapport.
- Interpréter les résultats d'une visualisation de données.

## 📅 Jour 9 – Introduction au Machine Learning

### 🎯 Objectifs
- Comprendre les bases du Machine Learning.
- Préparer les données pour un modèle.
- Entraîner un premier modèle de classification.
- Prédire le diagnostic d'une tumeur.
- Évaluer les performances du modèle.

### 📚 Notions étudiées
- Features (`X`)
- Target (`y`)
- `train_test_split()`
- `StandardScaler()`
- `LogisticRegression()`
- `fit()`
- `predict()`
- `accuracy_score()`
- `confusion_matrix()`
- `classification_report()`

### 🤖 Étapes réalisées
- Séparation des variables explicatives et de la variable cible.
- Découpage du dataset en jeu d'entraînement et jeu de test.
- Standardisation des données.
- Entraînement d'un modèle de régression logistique.
- Réalisation de prédictions sur les données de test.
- Évaluation des performances du modèle.

### 📈 Compétences acquises
À la fin de cette journée, je suis capable de :
- Préparer un dataset pour le Machine Learning.
- Comprendre la différence entre entraînement et test.
- Construire un premier modèle de classification.
- Effectuer des prédictions sur de nouvelles données.
- Évaluer un modèle grâce à plusieurs métriques.
- Interpréter les performances d'un modèle de Machine Learning.

## 📅 À venir



---

## 🛠️ Technologies

- Python
- Visual Studio Code
- Git
- GitHub


