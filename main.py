from utilisateur import (ajouter_utilisateur, supprimer_utilisateur,
                         modifier_mot_de_passe, statistiques, donnees_test)
from affichage import (afficher_menu_principal, afficher_non_respect_consigne,
                       afficher_liste_utilisateurs, afficher_aucun_utilisateur)
#from validation


# Menu principal
liste_utilisateurs = []
choix_menu = ["000","1", "2", "3", "4", "5", "6"]
numero = ""

while not numero == "6": # Tant que l'utilisateur ne souhaite pas fermer le programme
    afficher_menu_principal()
    numero = input("Indiquez le numéro correspondant à la fonctionnalité que vous souhaitez utiliser"
                   "\n Numéro 👉 ")
    if not numero in choix_menu:
        afficher_non_respect_consigne()
    else:

        # Accès aux différentes fonctionnalités
        if numero == "1":
            liste_utilisateurs = ajouter_utilisateur(liste_utilisateurs)

        if numero in ("2", "3", "4", "5"):
            if not liste_utilisateurs: # Entrée impossible si la liste est vide
                afficher_aucun_utilisateur()
            else:

                if numero == "2": # Supprimer un utilisateur
                    liste_utilisateurs = supprimer_utilisateur(liste_utilisateurs)

                if numero == "3": # Modifier le mot de passe d'un utilisateur
                    liste_utilisateurs = modifier_mot_de_passe(liste_utilisateurs)

                if numero == "4": # Afficher les utilisateurs
                    afficher_liste_utilisateurs(liste_utilisateurs)
                    sortir = input("\nSaisissez n'importe quel caractère pour revenir au menu principal"
                                   "\n👉 ")

                if  numero == "5":
                    statistiques(liste_utilisateurs)

        if numero == "000":
            liste_utilisateurs = donnees_test(liste_utilisateurs)
            print("✅✅✅ Les données test ont été intégrées ✅✅✅")

print("\n\n💤💤💤 Fin du programme 💤💤💤")