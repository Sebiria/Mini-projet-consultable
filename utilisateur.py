from affichage import (afficher_consignes_prenom, afficher_liste_erreur,
                       afficher_consignes_age, afficher_consignes_mot_de_passe,
                       afficher_consigne_confirmation_procedure)
from validation import (validation_prenom, validation_age, validation_mot_de_passe,
                        validation_confirmation_procedure)


def ajouter_utilisateur(liste_utilisateurs):
    print("\n\n🔹🔹🔹🔹🔹AJOUTER UN UTILISATEUR🔹🔹🔹🔹🔹")

    utilisateur = {"prenom": "", "age": 0, "mot_de_passe": "", "securite": ""}

    while True: # Tant que le prénom n'est pas valide
        afficher_consignes_prenom()
        prenom = input("Prenom : ").upper()
        erreurs = validation_prenom(prenom)
        if prenom == "SORTIR": # Si on veut revenir au menu principal
            return liste_utilisateurs
        elif erreurs: # Si le prénom n'est pas valide
            afficher_liste_erreur(erreurs)
        else: # Si le prénom est valide
            utilisateur['prenom'] = prenom
            break

    while True: # Tant que l'âge n'est pas valide
        afficher_consignes_age()
        age = input("Age : ")
        erreurs = validation_age(age)
        if age.upper() == "SORTIR": # Si on veut revenir au menu principal
            return liste_utilisateurs
        elif erreurs: # Si l'âge n'est pas valide
            afficher_liste_erreur(erreurs)
        else: # Si l'âge est valide
            utilisateur['age'] = int(age)
            break

    while True: # Tant que le mot de passe n'est pas valide
        afficher_consignes_mot_de_passe()
        mot_de_passe = input("Mot de passe : ")
        erreurs = validation_mot_de_passe(mot_de_passe)
        if prenom.upper() == "SORTIR":
            return liste_utilisateurs
        elif erreurs:
            afficher_liste_erreur(erreurs)
        else:
            utilisateur['mot_de_passe'] = mot_de_passe
            utilisateur['securite'] = "Faible" if len(mot_de_passe) <= 9 else "Moyen" if len(mot_de_passe) <= 11 else "Fort"
            break

    while True: # Tant que la confirmation n'est pas valide
        procedure = "d'ajout d'un utilisateur"
        afficher_consigne_confirmation_procedure(procedure, utilisateur['prenom'])
        confirmation = input("Confirmation : ").lower()
        erreurs = validation_confirmation_procedure(confirmation)
        if erreurs:
            afficher_liste_erreur(erreurs)
        else:
            if confirmation == "oui":
                liste_utilisateurs.append(utilisateur)
                return liste_utilisateurs
            else:
                return liste_utilisateurs