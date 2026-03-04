def validation_choix_fonctionnalite(choix):
    erreurs = []
    choix_menu = ["000", "1", "2", "3", "4", "5", "6"]
    if not choix.isdigit():
        erreurs.append("\033[31m- Ne doit contenir que des chiffres\033[0m")
    elif choix not in choix_menu:
        erreurs.append("\033[31m- Doit être compris entre 1 et 6\033[0m")
    return erreurs

def validation_prenom(prenom):
    erreurs = []
    if not prenom.isalpha():
        erreurs.append("\033[31m- Doit être entièrement composé de lettres\033[0m")
    if len(prenom) < 2:
        erreurs.append("\033[31m- Doit contenir au moins 2 caractères\033[0m")
    if " " in prenom:
        erreurs.append("\033[31m- Ne doit contenir aucun espace\033[0m")
    return erreurs

def validation_age(age):
    erreurs = []
    if not age.isdigit():
        erreurs.append("\033[31m- Ne doit contenir que des chiffres\033[0m")
    elif not 18 <= int(age) <= 120:
        erreurs.append("\033[31m- Doit être compris entre 18 et 120 ans\033[0m")
    if " " in age:
        erreurs.append("\033[31m- Ne doit contenir aucun espace\033[0m")
    return erreurs

def validation_mot_de_passe(mot_de_passe):
    erreurs = ["\033[31m- Doit contenir au moins 8 caractères\033[0m",
               "\033[31m- Doit contenir au moins une majuscule\033[0m",
               "\033[31m- Doit contenir au moins une minuscule\033[0m",
               "\033[31m- Doit contenir au moins un chiffre\033[0m",
               "\033[31m- Doit contenir au moins un caractère spécial (parmi => !@#$%&*)\033[0m",
               "\033[31m- Ne doit contenir aucun espace\033[0m"]

    # Si le critère est rempli, on le retire de la liste des erreurs
    if len(mot_de_passe) >= 8:
        if "\033[31m- Doit contenir au moins 8 caractères\033[0m" in erreurs:
            erreurs.remove("\033[31m- Doit contenir au moins 8 caractères\033[0m")
    if not " " in mot_de_passe:
        if "\033[31m- Ne doit contenir aucun espace\033[0m" in erreurs:
            erreurs.remove("\033[31m- Ne doit contenir aucun espace\033[0m")

    for caractere in mot_de_passe:
        if caractere.isupper():
            if "\033[31m- Doit contenir au moins une majuscule\033[0m" in erreurs:
                erreurs.remove("\033[31m- Doit contenir au moins une majuscule\033[0m")
        elif caractere.islower():
            if "\033[31m- Doit contenir au moins une minuscule\033[0m" in erreurs:
                erreurs.remove("\033[31m- Doit contenir au moins une minuscule\033[0m")
        elif caractere.isdigit():
            if "\033[31m- Doit contenir au moins un chiffre\033[0m" in erreurs:
                erreurs.remove("\033[31m- Doit contenir au moins un chiffre\033[0m")
        elif caractere in ("!@#$%&*"):
            if "\033[31m- Doit contenir au moins un caractère spécial (parmi => !@#$%&*)\033[0m" in erreurs:
                erreurs.remove("\033[31m- Doit contenir au moins un caractère spécial (parmi => !@#$%&*)\033[0m")
    return erreurs

def validation_confirmation_procedure(confirmation):
    erreurs = []
    if not confirmation in ("oui", "non"):
        erreurs.append("\033[31m- Doit être 'oui' ou 'non'\033[0m")
    return erreurs