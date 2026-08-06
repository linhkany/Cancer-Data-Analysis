# Concepts

## DataFrame

Tableau de données comparable à une feuille Excel.

## Series

Une seule colonne d'un DataFrame.

## Dataset

Ensemble de données utilisé pour une analyse.

## Observation

Une ligne du DataFrame.

Dans notre projet :
1 observation = 1 patient.

## Feature

Une caractéristique d'un patient.

Exemple :
- âge
- texture
- rayon

## Target

Variable que l'on cherche à prédire.

Dans notre projet :

0 = malignant
1 = benign

## Mean

Moyenne.

## Median

Médiane.

## Standard deviation

Écart-type.

Mesure la dispersion des données autour de la moyenne.

## Index

Numéro d'une ligne dans le DataFrame.

## Colonne

Variable décrivant chaque observation.

## Outils 
Python → le langage de programmation 🐍
Pandas → une bibliothèque pour manipuler des tableaux de données 📊
Matplotlib → une bibliothèque pour créer des graphiques 📈
Scikit-Learn → une bibliothèque pour entraîner des modèles d'intelligence artificielle 🤖

avec Pandas :
Lire les données
Les nettoyer
Les trier
Les filtrer
Les analyser

Puis, quand les données sont prêtes, Scikit-Learn prend le relais :

Séparer les données en entraînement et test
Créer un modèle
L'entraîner
Faire des prédictions
Évaluer ses performances

Chaque bibliothèque aura un rôle précis :

🐍 Python

Écrire le programme.

📊 Pandas

Manipuler et analyser les données.

📈 Matplotlib

Créer des graphiques.

🤖 Scikit-Learn

Construire et entraîner le modèle de Machine Learning.

### Machine Learning
La différence entre machine learning et le code normal est: Pour le code normal, on connaît la règle et on écrit la condition nous même.
Pour le machine learning, on ne connaît pas la règle, et à partir des exemples et des données le modèle cherche lui même une règle qui sépare ce qu'on veut prédire (dans notre projet tumeurs malignes et bénignes).

Features: Les informations d'entrée, nos colonnes avec les caractéristiques du tumeur.
Target: Ce qu'on veut prédire, maligne ou bénigne.

