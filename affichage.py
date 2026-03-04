#region Menu principal
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
#endregion

#region Consignes
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

def afficher_consigne_confirmation_procedure(procedure, prenom):
      print(f"\n\nIndiquez 👉oui/non👈 pour la confirmation de {procedure} s'agissant de {prenom}")
#endregion



def afficher_liste_erreur(erreurs):
      print("\n\n\033[31mVotre saisi n'est pas valide pour les raisons suivantes:\033[0m")
      for erreur in erreurs:
            print(erreur)

def afficher_revenir_menu_principal():
      print("\033[33mPour revenir au menu principal, tapez 👉SORTIR👈\033[0m")