from validation import (validation_prenom, validation_age,
                        validation_mot_de_passe, validation_selection_dans_resultat,
                        recherche_de_correlation, validation_chiffre_statistiques, oui_non)
from affichage import (afficher_liste_erreur, afficher_consigne_prenom,
                       afficher_consigne_age, afficher_consigne_mot_de_passe,
                       afficher_consigne_recherche_par_prenom,
                       afficher_resultat_recherche, afficher_consigne_selection_dans_resultat,
                       afficher_revenir_menu_principal, afficher_non_respect_consigne,
                       afficher_consigne_statistiques, afficher_statistiques)

def ajouter_utilisateur(liste_utilisateurs):
    print("\n\n🔹🔹🔹🔹🔹\033[36mAJOUTER UN UTILISATEUR\033[0m🔹🔹🔹🔹🔹")
    utilisateur = []

    # Saisie du prénom
    prenom_valide = False
    while not prenom_valide: # Tant qu'un prénom valide n'est pas saisi
        afficher_consigne_prenom()
        prenom = input("Prénom 👉 ")
        erreur = validation_prenom(prenom)
        if prenom.upper() == "SORTIR": # Si l'utilisateur souhaite revenir au menu principal
            return liste_utilisateurs
        elif erreur: # Si la liste des erreurs n'est pas vide
            afficher_liste_erreur(erreur)
        else:# Si la liste des erreurs est vide
            utilisateur.append(prenom.upper())
            print(f"\n\n✅✅✅ Le prénom {prenom.upper()} est valide ✅✅✅")
            prenom_valide = True

    #Saisie de l'âge
    age_valide = False
    while not age_valide: # Tant qu'un âge valide n'est pas saisi
        afficher_consigne_age()
        age = input("Prénom 👉 ")
        erreur = validation_age(age)
        if age.upper() == "SORTIR":
            return liste_utilisateurs
        elif erreur:
            afficher_liste_erreur(erreur)
        else:
            utilisateur.append(int(age))
            print(f"\n\n✅✅✅ L'âge de {int(age)} ans est valide ✅✅✅")
            age_valide = True

    # Saisie du mot de passe et affectation de son niveau de sécurité
    mot_de_passe_valide = False
    while not mot_de_passe_valide: # Tant qu'un mot de passe valide n'est pas saisi
        afficher_consigne_mot_de_passe()
        mot_de_passe = input("Mot de passe 👉 ")
        erreur = validation_mot_de_passe(mot_de_passe)
        if mot_de_passe.upper() == "SORTIR":
            return liste_utilisateurs
        elif erreur:
            afficher_liste_erreur(erreur)
        else:
            utilisateur.append(mot_de_passe)
            print(f"\n\n✅✅✅ Le mot de passe {mot_de_passe} est valide ✅✅✅")
            mot_de_passe_valide = True

            if len(utilisateur[2]) <= 9: # Attribution du niveau de sécurité du mot de passe
                utilisateur.append("Faible")
            elif len(utilisateur[2]) <=11:
                utilisateur.append("Moyen")
            else:
                utilisateur.append("Fort")
            print(f"✅✅✅ Le niveau de sécurité du mot de passe est {utilisateur[-1]} ✅✅✅")

    # Valider l'ajout du nouvel utilisateur à la liste
    while True:
        reponse = input(f"\n\nSouhaitez-vous ajouter à la liste l'utilisateur {utilisateur[0]}, {utilisateur[1]} ans"
                        f"\nMot de passe => {utilisateur[2]} - Niveau de sécurité => {utilisateur[3]}"
                        f"\noui/non 👉 ").lower()
        erreur = oui_non(reponse)
        if erreur:
            afficher_liste_erreur(erreur)
        else:
            if reponse == "oui":
                liste_utilisateurs.append(utilisateur)
                print(f"✅✅✅ L'utilisateur {utilisateur[0]} a bien été ajouté à la liste ✅✅✅")
            else:
                print(f"❌❌❌ L'utilisateur {utilisateur[0]} n'a pas été ajouté à la liste ❌❌❌")
            return liste_utilisateurs

def supprimer_utilisateur(liste_utilisateurs):
    print("\n\n🔹🔹🔹🔹🔹\033[36mSUPPRIMER UN UTILISATEUR\033[0m🔹🔹🔹🔹🔹")

    # Recherche dans les prénoms
    liste_index = []
    recherche_valide = False
    while not recherche_valide:
        afficher_consigne_recherche_par_prenom()
        afficher_revenir_menu_principal()
        prenom = input("Prenom 👉 ").upper()
        liste_index = recherche_de_correlation(prenom, liste_utilisateurs)
        if prenom == "SORTIR":
            return liste_utilisateurs
        elif not prenom.isalpha():
            afficher_non_respect_consigne()
        else:
            afficher_resultat_recherche(liste_index, liste_utilisateurs)
            if liste_index:
                recherche_valide = True

    numero = ""
    numero_valide = False
    while not numero_valide: # Selection du bon utilisateur
        afficher_consigne_selection_dans_resultat()
        afficher_revenir_menu_principal()
        numero = input("Numero 👉 ")
        if numero.upper() == "SORTIR":
            return liste_utilisateurs
        erreur = validation_selection_dans_resultat(numero, liste_index)
        if erreur:
            afficher_liste_erreur(erreur)
        else:
            numero_valide = True

    # Confirmation de la suppression
    while True:
        print(f"\n\nSouhaitez-vous supprimer l'utilisateur {liste_utilisateurs[int(numero)][0]}, {liste_utilisateurs[int(numero)][1]} ans")
        reponse = input("oui/non 👉 ").lower()
        oui_non(reponse)
        erreur = oui_non(reponse)
        if erreur:
            afficher_liste_erreur(erreur)
        else:
            if reponse == "oui":
                print(f"\n\n✅✅✅ L'utilisateur {liste_utilisateurs[int(numero)][0]} a bien été supprimé à la liste ✅✅✅")
                liste_utilisateurs.remove(liste_utilisateurs[int(numero)])
            else:
                print(f"\n\n❌❌❌ L'utilisateur {liste_utilisateurs[int(numero)][0]} n'a pas été supprimé à la liste ❌❌❌")
            return liste_utilisateurs

def modifier_mot_de_passe(liste_utilisateurs):
    print("\n\n🔹🔹\033[36mMODIFIER LE MOT DE PASSE D'UN UTILISATEUR\033[0m🔹🔹")

    # Recherche dans les prenoms
    liste_index = []
    recherche_valide = False
    while not recherche_valide:
        afficher_consigne_recherche_par_prenom()
        afficher_revenir_menu_principal()
        prenom = input("Prenom 👉 ").upper()
        liste_index = recherche_de_correlation(prenom, liste_utilisateurs)
        if prenom == "SORTIR":
            return liste_utilisateurs
        elif not prenom.isalpha():
            afficher_non_respect_consigne()
        else:
            afficher_resultat_recherche(liste_index, liste_utilisateurs)
            if liste_index:
                recherche_valide = True

    numero = ""
    numero_valide = False
    while not numero_valide: # Selection du bon utilisateur
        afficher_consigne_selection_dans_resultat()
        afficher_revenir_menu_principal()
        numero = input("Numero 👉 ")
        if numero.upper() == "SORTIR":
            return liste_utilisateurs
        erreur = validation_selection_dans_resultat(numero, liste_index)
        if erreur:
            afficher_liste_erreur(erreur)
        else:
            numero_valide = True

    # Saisie du mot de passe et affectation de son niveau de sécurité
    nouveau_mot_de_passe = []
    mot_de_passe_valide = False
    while not mot_de_passe_valide:  # Tant qu'un mot de passe valide n'est pas saisi
        afficher_consigne_mot_de_passe()
        mot_de_passe = input("Mot de passe 👉 ")
        erreur = validation_mot_de_passe(mot_de_passe)
        if mot_de_passe.upper() == "SORTIR":
            return liste_utilisateurs
        elif erreur:
            afficher_liste_erreur(erreur)
        else:
            nouveau_mot_de_passe.append(mot_de_passe)
            print(f"\n\n✅✅✅ Le nouveau mot de passe {mot_de_passe} est valide ✅✅✅")
            mot_de_passe_valide = True

            if len(nouveau_mot_de_passe[0]) <= 9: # Attribution du niveau de sécurité du mot de passe
                nouveau_mot_de_passe.append("Faible")
            elif len(nouveau_mot_de_passe[0]) <= 11:
                nouveau_mot_de_passe.append("Moyen")
            else:
                nouveau_mot_de_passe.append("Fort")
            print(f"✅✅✅ Le niveau de sécurité du nouveau mot de passe est {nouveau_mot_de_passe[1]} ✅✅✅")

    # Valider la modification du mot de passe
    while True:
        reponse = input(
            f"\n\nSouhaitez-vous modifier le mot de passe de l'utilisateur {liste_utilisateurs[int(numero)][0]} par:"
            f"\nNouveau mot de passe => {nouveau_mot_de_passe[0]} - Niveau de sécurité => {nouveau_mot_de_passe[1]}"
            f"\noui/non 👉 ").lower()
        erreur = oui_non(reponse)
        if erreur:
            afficher_liste_erreur(erreur)
        else:
            if reponse == "oui":
                liste_utilisateurs[int(numero)][2] = nouveau_mot_de_passe[0]
                liste_utilisateurs[int(numero)][3] = nouveau_mot_de_passe[1]
                print(f"✅✅✅ Le mot de passe de l'utilisateur {liste_utilisateurs[int(numero)]} a bien été changé ✅✅✅")
            else:
                print(f"❌❌❌ Le mot de passe de l'utilisateur {liste_utilisateurs[int(numero)]} n'a pas été changé ❌❌❌")
            return liste_utilisateurs

def statistiques(liste_utilisateurs):
    print("\n\n🔹🔹\033[36mSTATISTIQUES\033[0m🔹🔹")

    while True: # Tant que le critère n'est pas selectionné
        afficher_consigne_statistiques()
        chiffre = input("Chiffre 👉 ")
        erreur = validation_chiffre_statistiques(chiffre)
        if chiffre.upper() == "SORTIR":
            return liste_utilisateurs
        else:
            if erreur:
                afficher_liste_erreur(erreur)
            else:
                afficher_statistiques(chiffre, liste_utilisateurs)

def donnees_test(liste_utilisateurs):
    liste_test= [
        ["SEBASTIEN", 35, "Azerty12#", "Faible"],
        ["ARTHUR", 18, "Azerty12#f", "Moyen"],
        ["CORENTIN", 65, "Azerty12#f", "Moyen"],
        ["GABRIELLE", 42, "Azerty12#", "Faible"],
        ["THIERRY", 89, "Azerty12#ert", "Fort"],
        ["WILLO", 31, "Azerty12#f", "Moyen"],
        ["FABIENNE", 52, "Azerty12#f", "Moyen"],
        ["HECTOR", 26, "Azerty12#f", "Moyen"],
        ["JEREMIE", 37, "Azerty12#ert", "Fort"],
        ["EMILIE", 79, "Azerty12#", "Faible"],
        ["ISABELLE", 43, "Azerty12#ert", "Fort"],
        ["NATHALIE", 30, "Azerty12#f", "Moyen"],
        ["PATRICIA", 38, "Azerty12#ert", "Fort"],
    ]
    for i in liste_test:
        liste_utilisateurs.append(i)
    return liste_utilisateurs

