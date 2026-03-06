# Menu principal
def afficher_menu_principal():
    print("🔹🔹🔹🔹🔹MENU PRINCIPAL🔹🔹🔹🔹🔹"
          "\n1 - Ajouter un utilisateur"
          "\n 2 - Supprimer un utilisateur"
          "\n  3 - Modifier le mot de passe"
          "\n   4 - Afficher les utilisateurs"
          "\n    5 - Statistiques"
          "\n     6 - Quitter le programme"
          "\nIndiquez le chiffre correspondant à la fonctionnalité souhaitée")

def afficher_liste_vide():
      print("😐 Certaines fonctionnalités sont bloquées "
            "puisque la liste des utilisateurs est vide 😐")

def afficher_liste_utilisateurs(liste_utilisateurs):
      print("\n\n🔹🔹🔹🔹AFFICHER LA LISTE DES UTILISATEURS🔹🔹🔹🔹")
      for index, utilisateur in enumerate(liste_utilisateurs):
            print(f"{index} - Prénom: {utilisateur['prenom']} - Age: {utilisateur['age']} - "
                  f"Mot de passe: {utilisateur['mot_de_passe']} - Niveau de sécurité: {utilisateur['niveau_securite']}")
      input("\033[33mPour revenir au menu principal, appuyez sur la touche ⚪ENTRÉE⚪\033[0m")

def afficher_statistiques(liste_utilisateurs):
      print("\n\n🔹🔹🔹🔹🔹AFFICHER LES STATISTIQUES🔹🔹🔹🔹🔹")

      compteur = {"moins_de_30_ans": 0, "plus_de_30_ans": 0,
                  "niveau-faible": 0, "niveau_moyen": 0, "niveau_fort": 0,
                  "longueur_total_mot_de_passe": 0}
      for utilisateur in liste_utilisateurs:
            compteur["moins_de_30_ans"] += 1 if utilisateur['age'] < 30 else 0
            compteur["plus_de_30_ans"] += 1 if utilisateur['age'] >= 30 else 0
            compteur["niveau-faible"] += 1 if utilisateur['niveau_securite'] == "Faible" else 0
            compteur["niveau-moyen"] += 1 if utilisateur['niveau_securite'] == "Moyen" else 0
            compteur["niveau-fort"] += 1 if utilisateur['niveau_securite'] == "Fort" else 0
            compteur["longueur_total_mot_de_passe"] += len(utilisateur['mot_de_passe'])

      print(f"\n\nLe nombre total d'utilisateurs est de 👉 {len(liste_utilisateurs)}")

      print(f"\nLe nombre d'utilisateurs de moins de 30 ans est de 👉 {compteur["moins_de_30_ans"]}"
            f"\nLe nombre d'utilisateurs de 30 ans et plus est de 👉 {compteur["plus_de_30_ans"]}")

      print(f"\nLe nombre d'utilisateurs de niveau de sécurité faible est de 👉 {compteur["niveau-faible"]}"
            f"\nLe nombre d'utilisateurs de niveau de sécurité moyen est de 👉 {compteur["niveau-moyen"]}"
            f"\nLe nombre d'utilisateurs de niveau de sécurité fort est de 👉 {compteur["niveau-fort"]}")

      print(f"\nLe taille moyenne des mots de passe est de 👉 {compteur["longueur_total_mot_de_passe"] / len(liste_utilisateurs)}")

      input("\n\033[33mPour revenir au menu principal, appuyez sur la touche ⚪ENTRÉE⚪\033[0m")


# Consignes
def afficher_consignes_prenom():
      print("\nIndiquez le prénom de l'utilisateur en respectant les consignes suivantes :"
            "\n- Doit contenir au moins 2 caractères"
            "\n- Doit être entièrement composé de lettres"
            "\n- Ne doit contenir aucun espace")
      afficher_revenir_menu_principal()

def afficher_consignes_age():
      print("\nIndiquez l'âge de l'utilisateur en respectant les consignes suivantes :"
            "\n- Doit être compris entre 18 et 120 ans"
            "\n- Doit être entièrement composé de chiffres"
            "\n- Ne doit contenir aucun espace")
      afficher_revenir_menu_principal()

def afficher_consignes_mot_de_passe():
      print("\nIndiquez le mot de passe de l'utilisateur en respectant les consignes suivantes :"
            "\n- Doit contenir au moins 8 caractères"
            "\n- Doit contenir au moins une majuscule"
            "\n- Doit contenir au moins une minuscule"
            "\n- Doit contenir au moins un chiffre"
            "\n- Doit contenir au moins un caractère spécial (parmi => !@#$%&*)"
            "\n- Ne doit contenir aucun espace")
      afficher_revenir_menu_principal()

def afficher_consignes_confirmation_procedure(procedure, prenom):
      print(f"\n\nIndiquez 👉oui/non👈 pour la confirmation de {procedure} s'agissant de \033[33m{prenom}\033[0m")

def afficher_consignes_recherche_par_prenom():
      print("Indiquez le prénom (ou en partie) de l'utilisateur en question")
      afficher_revenir_menu_principal()

def afficher_consignes_selection_utilisateur():
      print("\nIndiquez le nombre qui précède le prenom de l'utilisateur en question")
      afficher_revenir_menu_principal()


# Divers
def afficher_liste_utilisateurs_trouves(liste_utilisateurs_trouves):
      print("\n\nListe des utilisateurs potentiels:")
      for index, utilisateur in enumerate(liste_utilisateurs_trouves):
            print(f"{index} - {utilisateur['prenom']} - {utilisateur['age']} ans")

def afficher_liste_erreur(erreurs):
      print("\n\n\033[31mVotre saisi n'est pas valide pour les raisons suivantes:\033[0m")
      for erreur in erreurs:
            print(erreur)

def afficher_revenir_menu_principal():
      print("\033[33mPour revenir au menu principal, tapez 👉SORTIR👈\033[0m")
      