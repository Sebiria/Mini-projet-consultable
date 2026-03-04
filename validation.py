def validation_prenom(prenom):
    erreur = ["\033[31mLe prénom doit contenir au moins 2 caractères\033[0m",
               "\033[31mLe prénom doit contenir que des lettres\033[0m",
               "\033[31mLe prénom doit contenir aucun espace\033[0m"]
    if len(prenom) >= 2:
        if "\033[31mLe prénom doit contenir au moins 2 caractères\033[0m" in erreur:
            erreur.remove("\033[31mLe prénom doit contenir au moins 2 caractères\033[0m")
    if not " " in prenom:
        if "\033[31mLe prénom doit contenir aucun espace\033[0m" in erreur:
            erreur.remove("\033[31mLe prénom doit contenir aucun espace\033[0m")
    if prenom.isalpha():
        if "\033[31mLe prénom doit contenir que des lettres\033[0m" in erreur:
            erreur.remove("\033[31mLe prénom doit contenir que des lettres\033[0m")
    return erreur

def validation_age(age):
    erreur = ["\033[31mUn nombre entre 18 et 120 ans\033[0m",
               "\033[31mNe doit contenir que des chiffres\033[0m",
               "\033[31mL'âge doit contenir aucun espace\033[0m"]
    if not " " in age:
        if "\033[31mL'âge doit contenir aucun espace\033[0m" in erreur:
            erreur.remove("\033[31mL'âge doit contenir aucun espace\033[0m")
    if age.isdigit():
        if "\033[31mNe doit contenir que des chiffres\033[0m" in erreur:
            erreur.remove("\033[31mNe doit contenir que des chiffres\033[0m")
        if 18 <= int(age) <= 120:
            if "\033[31mUn nombre entre 18 et 120 ans\033[0m" in erreur:
                erreur.remove("\033[31mUn nombre entre 18 et 120 ans\033[0m")
    return erreur

def validation_mot_de_passe(mot_de_passe):
    erreur = ["\033[31mAu moins 8 caractères\033[0m",
              "\033[31mAu moins 1 majuscule\033[0m",
              "\033[31mAu moins 1 minuscule\033[0m",
              "\033[31mAu moins 1 chiffres\033[0m",
              "\033[31mAu moins 1 caractère spécial (parmi => ! @ # $ % & *)\033[0m",
              "\033[31mLe mot de passe ne doit contenir aucun espace\033[0m"]
    if not " " in mot_de_passe:
        erreur.remove("\033[31mLe mot de passe ne doit contenir aucun espace\033[0m")
    if len(mot_de_passe) >= 8:
        erreur.remove("\033[31mAu moins 8 caractères\033[0m")
    for i in mot_de_passe:
        if i.isupper():
            if "\033[31mAu moins 1 majuscule\033[0m" in erreur:
                erreur.remove("\033[31mAu moins 1 majuscule\033[0m")
        elif i.islower():
            if "\033[31mAu moins 1 minuscule\033[0m" in erreur:
                erreur.remove("\033[31mAu moins 1 minuscule\033[0m")
        elif i.isdigit():
            if "\033[31mAu moins 1 chiffres\033[0m" in erreur:
                erreur.remove("\033[31mAu moins 1 chiffres\033[0m")
        elif i in "!@#$%&*":
            if "\033[31mAu moins 1 caractère spécial (parmi => ! @ # $ % & *)\033[0m" in erreur:
                erreur.remove("\033[31mAu moins 1 caractère spécial (parmi => ! @ # $ % & *)\033[0m")
    return erreur

def recherche_de_correlation(prenom, liste_utilisateurs):
    liste_index = []
    iteration = 0
    for i in liste_utilisateurs:
        if prenom in i[0]:
            liste_index.append(iteration)
        iteration += 1
    return liste_index

def validation_selection_dans_resultat(numero, liste_index):
    erreur = ["\033[31mLe nombre doit correspondre au résultat affiché\033[0m",
              "\033[31mNe doit contenir que des chiffres\033[0m",
              "\033[31mL'indication doit contenir aucun espace\033[0m"]
    if not " " in numero:
        if "\033[31mL'indication doit contenir aucun espace\033[0m" in erreur:
            erreur.remove("\033[31mL'indication doit contenir aucun espace\033[0m")
    if numero.isdigit():
        if "\033[31mNe doit contenir que des chiffres\033[0m" in erreur:
            erreur.remove("\033[31mNe doit contenir que des chiffres\033[0m")
        if int(numero) in liste_index:
            if "\033[31mLe nombre doit correspondre au résultat affiché\033[0m" in erreur:
                erreur.remove("\033[31mLe nombre doit correspondre au résultat affiché\033[0m")
    return erreur

def validation_chiffre_statistiques(chiffre):
    erreur = ["\033[31mLe nombre doit correspondre au résultat affiché\033[0m",
              "\033[31mNe doit contenir que des chiffres\033[0m",
              "\033[31mL'indication doit contenir aucun espace\033[0m"]
    if not " " in chiffre:
        if "\033[31mL'indication doit contenir aucun espace\033[0m" in erreur:
            erreur.remove("\033[31mL'indication doit contenir aucun espace\033[0m")
    if chiffre.isdigit():
        if "\033[31mNe doit contenir que des chiffres\033[0m" in erreur:
            erreur.remove("\033[31mNe doit contenir que des chiffres\033[0m")
        if chiffre in ("1", "2", "3", "4"):
            if "\033[31mLe nombre doit correspondre au résultat affiché\033[0m" in erreur:
                erreur.remove("\033[31mLe nombre doit correspondre au résultat affiché\033[0m")
    return erreur

def oui_non(reponse):
    erreur = []
    if reponse not in ("oui", "non"):
        erreur.append("\033[31mVotre réponse ne peut être que oui ou non\033[0m")
    if " " in reponse:
        erreur.append("\033[31mVotre réponse ne doit contenir aucun espace\033[0m")
    return erreur