from affichage import (afficher_consignes_prenom, afficher_liste_erreur,
                       afficher_consignes_age, afficher_consignes_mot_de_passe,
                       afficher_consignes_confirmation_procedure, afficher_consignes_recherche_par_prenom,
                       afficher_liste_utilisateurs_trouves, afficher_consignes_selection_utilisateur)
from validation import (validation_prenom, validation_age, validation_mot_de_passe,
                        validation_confirmation_procedure, validation_recherche_par_critere,
                        validation_selection_du_bon_utilisateur)
from stockage import sauvegarder_utilisateurs

def ajouter_utilisateur(liste_utilisateurs):
    print("\n\n🔹🔹🔹🔹🔹AJOUTER UN UTILISATEUR🔹🔹🔹🔹🔹")

    utilisateur = {"prenom": "", "age": 0, "mot_de_passe": "", "niveau_securite": ""}

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
        if mot_de_passe.upper() == "SORTIR":
            return liste_utilisateurs
        elif erreurs:
            afficher_liste_erreur(erreurs)
        else:
            utilisateur['mot_de_passe'] = mot_de_passe
            utilisateur['niveau_securite'] = "Faible" if len(mot_de_passe) <= 9 else "Moyen" if len(mot_de_passe) <= 11 else "Fort"
            break

    while True: # Tant que la confirmation n'est pas valide
        procedure = "d'ajout d'un utilisateur"
        afficher_consignes_confirmation_procedure(procedure, utilisateur['prenom'])
        confirmation = input("Confirmation : ").lower()
        erreurs = validation_confirmation_procedure(confirmation)
        if erreurs:
            afficher_liste_erreur(erreurs)
        else:
            if confirmation == "oui":
                liste_utilisateurs.append(utilisateur)
                print(f"✅✅✅ L'utilisateur {utilisateur['prenom']} a bien été ajouté ✅✅✅")
                sauvegarder_utilisateurs(liste_utilisateurs)
                return liste_utilisateurs
            else:
                print(f"❌❌❌ L'utilisateur {utilisateur['prenom']} n'a pas été ajouté ❌❌❌")
                return liste_utilisateurs

def supprimer_utilisateur(liste_utilisateurs):
    print("\n\n🔹🔹🔹🔹🔹SUPPRIMER UN UTILISATEUR🔹🔹🔹🔹🔹")

    critere = 'prenom'
    while True: # Tant que le prenom (ou une partie) n'est pas saisi
        afficher_consignes_recherche_par_prenom()
        prenom = input("Prenom 👉 ")
        liste_utilisateurs_trouves = validation_recherche_par_critere(prenom, liste_utilisateurs, critere)
        if prenom.upper() == "SORTIR": # Si l'utilisateur souhaite revenir au menu principal
            return liste_utilisateurs
        elif not liste_utilisateurs_trouves: # S'il n'y a pas de correspondance
            print("\n\n😐 Aucun utilisateur ne correspond à votre indication 😐")
        else:# S'il y a des correspondances
            break


    while True: # Tant que l'un des utilisateurs trouvés n'a pas été selectionné
        afficher_liste_utilisateurs_trouves(liste_utilisateurs_trouves)
        afficher_consignes_selection_utilisateur()
        nombre = input("Nombre 👉 ")
        erreurs = validation_selection_du_bon_utilisateur(nombre, liste_utilisateurs_trouves)
        if nombre.upper() == "SORTIR":
            return liste_utilisateurs
        elif erreurs:
            afficher_liste_erreur(erreurs)
        else:
            break

    while True:  # Tant que la confirmation n'est pas valide
        utilisateur = liste_utilisateurs_trouves[int(nombre)]
        procedure = "suppression d'utilisateur"
        afficher_consignes_confirmation_procedure(procedure, utilisateur['prenom'])
        confirmation = input("Confirmation : ").lower()
        erreurs = validation_confirmation_procedure(confirmation)
        if erreurs:
            afficher_liste_erreur(erreurs)
        else:
            if confirmation == "oui":
                liste_utilisateurs.remove(utilisateur)
                print(f"✅✅✅ L'utilisateur {utilisateur['prenom']} a bien été supprimé ✅✅✅")
                sauvegarder_utilisateurs(liste_utilisateurs)
                return liste_utilisateurs
            else:
                print(f"❌❌❌ L'utilisateur {utilisateur['prenom']} n'a pas été supprimé ❌❌❌")
                return liste_utilisateurs

def modifier_mot_de_passe_utilisateur(liste_utilisateurs):
    print("\n\n🔹🔹MODIFIER LE MOT DE PASSE D'UN UTILISATEUR🔹🔹")

    nouveau_mot_de_passe = {"nouveau_mot_de_passe": "", "niveau_securite": ""}
    index_utilisateur = 0
    critere = 'prenom'
    while True:  # Tant que le prenom (ou une partie) n'est pas saisi
        afficher_consignes_recherche_par_prenom()
        prenom = input("Prenom 👉 ")
        liste_utilisateurs_trouves = validation_recherche_par_critere(prenom, liste_utilisateurs, critere)
        if prenom.upper() == "SORTIR":  # Si l'utilisateur souhaite revenir au menu principal
            return liste_utilisateurs
        elif not liste_utilisateurs_trouves:  # S'il n'y a pas de correspondance
            print("\n\n😐 Aucun utilisateur ne correspond à votre indication 😐")
        else:  # S'il y a des correspondances
            break

    while True:  # Tant que l'un des utilisateurs trouvés n'a pas été selectionné
        afficher_liste_utilisateurs_trouves(liste_utilisateurs_trouves)
        afficher_consignes_selection_utilisateur()
        nombre = input("Nombre 👉 ")
        erreurs = validation_selection_du_bon_utilisateur(nombre, liste_utilisateurs_trouves)
        if nombre.upper() == "SORTIR":
            return liste_utilisateurs
        elif erreurs:
            afficher_liste_erreur(erreurs)
        else:
            utilisateur = liste_utilisateurs_trouves[int(nombre)]
            for index, personne in enumerate(liste_utilisateurs):
                if utilisateur == personne:
                    index_utilisateur = index
                    break
            break

    while True: # Tant que le mot de passe n'est pas valide
        afficher_consignes_mot_de_passe()
        mot_de_passe = input("Mot de passe : ")
        erreurs = validation_mot_de_passe(mot_de_passe)
        if mot_de_passe.upper() == "SORTIR":
            return liste_utilisateurs
        elif erreurs:
            afficher_liste_erreur(erreurs)
        else:
            nouveau_mot_de_passe['nouveau_mot_de_passe'] = mot_de_passe
            nouveau_mot_de_passe['niveau_securite'] = "Faible" if len(mot_de_passe) <= 9 else "Moyen" if len(mot_de_passe) <= 11 else "Fort"

            break

    while True: # Tant que la confirmation n'est pas valide
        procedure = "modification de mot de passe"
        afficher_consignes_confirmation_procedure(procedure, utilisateur['prenom'])
        confirmation = input("Confirmation : ").lower()
        erreurs = validation_confirmation_procedure(confirmation)
        if erreurs:
            afficher_liste_erreur(erreurs)
        else:
            if confirmation == "oui":
                liste_utilisateurs[index_utilisateur]['mot_de_passe'] = nouveau_mot_de_passe['nouveau_mot_de_passe']
                liste_utilisateurs[index_utilisateur]['niveau_securite'] = nouveau_mot_de_passe['niveau_securite']
                print(f"✅✅✅ Le mot de passe de l'utilisateur {utilisateur['prenom']} a bien été changé ✅✅✅")
                return liste_utilisateurs
            else:
                print(f"❌❌❌ Le mot de passe de l'utilisateur {utilisateur['prenom']} n'a pas été changé ❌❌❌")
                sauvegarder_utilisateurs(liste_utilisateurs)
                return liste_utilisateurs

def implementer_donnees_test(liste_utilisateurs):
    liste = [
        {"prenom": "SEBASTIEN", "age": 35, "mot_de_passe": "Azerty12#", "niveau_securite": "Faible"},
        {"prenom": "ARTHUR", "age": 18, "mot_de_passe": "Azerty12#f", "niveau_securite": "Moyen"},
        {"prenom": "CORENTIN", "age": 65, "mot_de_passe": "Azerty12#f", "niveau_securite": "Moyen"},
        {"prenom": "GABRIELLE", "age": 42, "mot_de_passe": "Azerty12#", "niveau_securite": "Faible"},
        {"prenom": "THIERRY", "age": 89, "mot_de_passe": "Azerty12#ert", "niveau_securite": "Fort"},
        {"prenom": "WILLO", "age": 31, "mot_de_passe": "Azerty12#f", "niveau_securite": "Moyen"},
        {"prenom": "FABIENNE", "age": 52, "mot_de_passe": "Azerty12#f", "niveau_securite": "Moyen"},
        {"prenom": "HECTOR", "age": 26, "mot_de_passe": "Azerty12#f", "niveau_securite": "Moyen"},
        {"prenom": "JEREMIE", "age": 37, "mot_de_passe": "Azerty12#ert", "niveau_securite": "Fort"},
        {"prenom": "EMILIE", "age": 79, "mot_de_passe": "Azerty12#", "niveau_securite": "Faible"},
        {"prenom": "ISABELLE", "age": 43, "mot_de_passe": "Azerty12#ert", "niveau_securite": "Fort"},
        {"prenom": "NATHALIE", "age": 30, "mot_de_passe": "Azerty12#f", "niveau_securite": "Moyen"},
        {"prenom": "PATRICIA", "age": 38, "mot_de_passe": "Azerty12#ert", "niveau_securite": "Fort"},
    ]
    for i in liste:
        liste_utilisateurs.append(i)
    sauvegarder_utilisateurs(liste_utilisateurs)
    print("✅✅✅ Données test effectifs ✅✅✅")
    return liste_utilisateurs