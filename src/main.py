#Jour1

print("Cancer Data Analysis")
print("mini-projet")

#Exercice 1
patient = "Kevin" #type de donnée: Texte(str)
age = 25 #type de donnée: Entier(int)
poids = 67.5 #type de donnée: Décimal(float)
diagnostic = "Malignant"
est_fumeur = False #type de donnée: Vrai/Faux(bool)

print(patient)
print(age)
print(poids)
print(diagnostic)
print(est_fumeur)

#Jour 2
#Exercice 2
#les opérateurs: + - * /

age = 22
print(age +5)
print(age -1)
print(age *2)
print(age /2)

age = age + 1
print(age)

#Calcul de l'IMC
#IMC = poids/taille^2

poids = float(input("Rentrez votre poids (kg): "))
taille = float(input("Rentrez votre taille (m): "))

imc = poids/(taille**2)
print("Votre IMC est: ", imc)
print("Votre IMC est: ", round(imc,2)) #la commande round sert à arrondir x chiffres après la virgule
if imc > 25: 
    print("Catégorie: surpoids")
elif imc <= 25 and imc >= 18.5:
    print("Catégorie: Poids Normal")
else: 
    print("Catégorie: Insuffisance pondérale")

#Jour 3
#Les listes
#Objectif d'avoir une liste c'est quand on a beaucoup de données, une liste pourra contenir beaucoup de valeurs. Utile dans le stockage de nombreux patients. 
patients = ["Marie", "Théo", "Angeline", "Laurent","Isabelle"]
print(patients)
print(patients[0]) # envoie le premier élément de la liste (Marie), les listes commencent à indice 0
print(patients[1]) # envoie Théo

patients[2] = "Gwendoline" # modifier un élément de la liste
patients.append("Kevin") # cette commande permet d'ajouter un élément dans la liste
patients.remove("Marie") # commande permettant d'enlever un élément

print(len(patients)) #longueur de la liste, permettant de connaître le nombre de patients.


#Exercice 3
liste_patients = ["Marie", "Paul", "Emma", "Lucas", "Sophie"]
print(liste_patients)
print(liste_patients[2])
liste_patients[2] = "Thomas"
liste_patients.append("Julie")
liste_patients.remove("Paul")
print(liste_patients)
print(len(liste_patients))

#Les boucles For
for patient in liste_patients:
    print("Patient:", patient)

#Exercice 4
patients2 = ["Lucie", "Guillaume", "Anthony", "Adam", "Gauthier"]
for patient in patients2:
    print(patient) #affiche tous les patients avec une boucle for
for patient in patients2:
    print("Bonjour", patient)
for patient in patients2:
    print("Patient enregistré: ", patient)

nombre_de_patients = len(patients2)
print("On a", nombre_de_patients, "patients au total.")

#Les dictionnaires
patient = {"nom": "Kevin", "âge": 25, "diagnostic": "Malignant" } #un dictionnaire est composé d'une clé suivi d'une valeur
print(patient) #afficher le dictionnaire
print(patient["nom"]) # Pour accéder à une information, on affiche le dictionnaire avec la clé voulu.    
patient["âge"] = 24 # modifier une valeur
patient["taille"] = 1.68
print(patient)

#Exercice 5
patient1 = {"nom": "Phong", "âge": 17, "diagnostic": "benign"}
print(patient1["nom"])
print(patient1["âge"])
print(patient1["diagnostic"])
patient1["âge"] = 46
patient1["poids"] = 62
print(patient1)

liste_dictionnaire_patient = [{"nom": "Khanh Linh", "âge": 22, "diagnostic": "benign"}, {"nom":"Kevin", "âge": 25, "diagnostic": "malign"}]
print(liste_dictionnaire_patient[0]) # envoie le premier dictionnaire
patient_femme = liste_dictionnaire_patient[0]
patient_homme = liste_dictionnaire_patient[1]
print(patient_femme["nom"])
print(patient_homme["diagnostic"])
patient_homme["poids"] = 70
patient_femme["poids"] = 50
print(liste_dictionnaire_patient)

#Défi du jour
patients = [{"nom": "Khanh Linh", "age": 22, "diagnostic": "B"}, {"nom": "Kevin", "age": 25, "diagnostic": "M"}, {"nom": "Emma", "age": 45, "diagnostic": "B"}]

i = 0
for i in range(3):
    print("Nom:", patients[i]["nom"])
    print("Age:", patients[i]["age"])
    print("Diagnostic:", patients[i]["diagnostic"])
    print()

#Autre façon
for patient in patients:
    print("Nom:", patient["nom"])
    print("Age:", patient["age"])
    print("Diagnostic:", patient["diagnostic"])
    print() #saut de ligne 


#Jour 4
#Les fonctions
from patients import *

patients = [{"nom": "Emma", "age": 45, "diagnostic": "B"},{"nom": "Kevin", "age": 25, "diagnostic": "M"}, {"nom": "Linh", "age": 22, "diagnostic": "B"}, {"nom": "Paul", "age": 58, "diagnostic": "M"}]

for patient in patients: 
    afficher_patient(patient)
    print()

#Exercice 6

print("Âge moyen:", age_moyen(patients), "ans")

print("Nombre de patients malins:", compter_malignant(patients))

print("L'âge maximum des patients est:", plus_age(patients))

print(est_majeur(20))
print(est_majeur(5))

print(est_mineur(17))

print(malins_patients(patients))
