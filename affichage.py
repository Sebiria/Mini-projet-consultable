def afficher_menu_principal():
    print("🔹🔹🔹🔹🔹\033[36mMENU PRINCIPAL\033[0m🔹🔹🔹🔹🔹"
          "\n1 - Ajouter un utilisateur"
          "\n2 - Supprimer un utilisateur"
          "\n3 - Modifier le mot de passe d'un utilisateur"
          "\n4 - Afficher les utilisateurs"
          "\n5 - Afficher les statistiques"
          "\n6 - Quitter le programme")

def afficher_revenir_menu_principal():
    print("Tapez \033[36mSORTIR\033[0m pour revenir au menu principal")

def afficher_non_respect_consigne():
    print("\n\n⚠️⚠️⚠️ \033[31mAttention à bien respecter la consigne ci-dessous\033[0m ⚠️⚠️⚠️")

def afficher_liste_erreur(erreur):
    print(f"\n\n\033[31mVotre saisi n'est pas bonne pour {"la raison suivante" if len(erreur) == 1 else "les raisons suivantes"} :\033[0m")
    for i in erreur:
        print(i)

def afficher_consigne_prenom():
    print("Indiquez le prénom du nouvel utilisateur selon les critères suivants :"
          "\n- Au moins 2 caractères"
          "\n- Ne doit contenir que des lettres"
          "\n- Ne doit contenir aucun espace")
    afficher_revenir_menu_principal()

def afficher_consigne_age():
    print("Indiquez l'âge du nouvel utilisateur selon les critères suivants :"
          "\n- Un nombre entre 18 et 120 ans"
          "\n- Ne doit contenir que des chiffres"
          "\n- Ne doit contenir aucun espace")
    afficher_revenir_menu_principal()

def afficher_consigne_mot_de_passe():
    print("Indiquez le mot de passe de l'utilisateur selon les critères suivants :"
          "\n- Au moins 8 caractères"
          "\n- Au moins 1 majuscule"
          "\n- Au moins 1 minuscule"
          "\n- Au moins 1 chiffres"
          "\n- Au moins 1 caractère spécial (parmi => ! @ # $ % & *)"
          "\n- Ne doit contenir aucun espace")
    afficher_revenir_menu_principal()

def afficher_aucun_utilisateur():
    print("\n\n\033[31mIl n'y a aucun utilisateur pour le moment\033[0m")

def afficher_liste_utilisateurs(liste_utilisateurs):
    print("\n\n🔹🔹🔹🔹🔹\033[36mAFFICHER LES UTILISATEURS\033[0m🔹🔹🔹🔹🔹")
    if liste_utilisateurs:
        for i in liste_utilisateurs:
            print(f"{i[0]}, {i[1]} ans - \033[36mMot de passe =>\033[0m {i[2]} - \033[36mNiveau de sécurité =>\033[0m {i[3]}")
    else:
        print("Il n'y a aucun utilisateur pour le moment.")

def afficher_consigne_recherche_par_prenom():
    print("Indiquez le prénom (ou une partie) de l'utilisateur en question")

def afficher_resultat_recherche(list_index, liste_utilisateurs):
    if not list_index:
        print("\n\n\033[31mIl n'y a aucun contact correspondant à ce que vous avez indiqué\033[0m")
    else:
        print("\n\nListe des utilisateurs correspondants à votre indication:")
        for i in list_index:
            print(f"{i} - {liste_utilisateurs[i][0]}, {liste_utilisateurs[i][1]} ans")

def afficher_consigne_selection_dans_resultat():
    print("\nIndiquez le numéro correspondant à l'utilisateur en question")

def afficher_consigne_statistiques():
    print("\nIndiquez le numéro correspondant au critère selon lequel vous souhaitez afficher les statistiques"
          "\n1 - Nombre total d'utilisateur"
          "\n 2 - Nombre d'utilisateur de moins de 30 ans, et 30 ans +"
          "\n  3 - Nombre d'utilisateur par niveau de sécurité"
          "\n   4 - Longueur moyenne des mots de passe")
    afficher_revenir_menu_principal()

def afficher_statistiques(chiffre, liste_utilisateurs):
    compteur_moins_de_30 = 0
    compteur_30_et_plus = 0
    compteur_faible = 0
    compteur_moyen = 0
    compteur_fort = 0
    for i in liste_utilisateurs:
        compteur_moins_de_30 += 1 if i[1] < 30 else 0
        compteur_30_et_plus += 1 if i[1] >= 30 else 0
        compteur_faible += 1 if i[3] == "Faible" else 0
        compteur_moyen += 1 if i[3] == "Moyen" else 0
        compteur_fort += 1 if i[3] == "Fort" else 0


    if chiffre == "1":
        print(f"\n\nNombre total d'utilisateur : {len(liste_utilisateurs)}")
    elif chiffre == "2":
        print(f"\n\nNombre d'utilisateur de moins de 30 ans : {compteur_moins_de_30}")
        print(f"Nombre d'utilisateur de 30 ans et plus : {compteur_30_et_plus}")
    elif chiffre == "3":
        print(f"\n\nNombre d'utilisateur de niveau de sécurité faible : {compteur_faible}")
        print(f"Nombre d'utilisateur de niveau de sécurité moyen : {compteur_moyen}")
        print(f"Nombre d'utilisateur de niveau de sécurité fort : {compteur_fort}")
    else:
        print(f"\n\nLongueur moyenne des mots de passe : {sum(len(i[2]) for i in liste_utilisateurs) / len(liste_utilisateurs)}")
