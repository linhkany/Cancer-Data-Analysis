#Jour 4
#Les fonctions
#Au lieu de faire 'print' pour chaque patient, on pourra faire appel à la fonction qui sera plus efficace; comme une commande raccourci 
def afficher_patient(patient):
    print("Nom:", patient["nom"])
    print("Age:", patient["age"])
    print("Diagnostic:", patient["diagnostic"])

def age_moyen(patients): 
    somme = 0
    for patient in patients: 
        somme = somme + patient["age"]  # La nouvelle somme = l'ancienne somme + l'âge du patient.
        
    moyenne = somme/len(patients)
    return moyenne

def compter_malignant(patients):
    compteur = 0
    for patient in patients:
        if patient["diagnostic"] == "M":
            compteur = compteur + 1 
    return compteur

def plus_age(patients):
    max = 0
    for patient in patients:
        if max <= patient["age"]:
            max = patient["age"]
    return max 

def est_majeur(age):
    if age >= 18:
        return True
    else: 
        return False

def est_mineur(age):
    return age < 18

def malins_patients(patients):
    malins = []
    for patient in patients:
        if patient["diagnostic"] == "M":
            malins.append(patient)
    return malins