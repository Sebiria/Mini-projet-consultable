from affichage import (afficher_menu_principal, afficher_liste_erreur, afficher_liste_vide,
                       afficher_liste_utilisateurs)
from utilisateur import ajouter_utilisateur, supprimer_utilisateur
from validation import validation_choix_fonctionnalite


if __name__ == "__main__":
    liste_utilisateurs = []

    while True: # Tant que le programme est en cours d'exécution
        afficher_menu_principal()
        choix = input("Votre choix : ")
        erreurs = validation_choix_fonctionnalite(choix)
        if erreurs:
            afficher_liste_erreur(erreurs)
        else:


            #ACCES AUX FONCTIONNALITES

            if choix == "1": # Ajouter un utilisateur
                liste_utilisateur = ajouter_utilisateur(liste_utilisateurs)

            elif not liste_utilisateurs:
                afficher_liste_vide()

            elif not choix == "6":

                if choix == "2":
                    liste_utilisateurs = supprimer_utilisateur(liste_utilisateurs)

                #if choix == "3":


                if choix == "4":  # Afficher la liste des utilisateurs
                    afficher_liste_utilisateurs(liste_utilisateurs)
                    input("\033[33mPour revenir au menu principal, appuyez sur la touche 👉ENTRÉE👈\033[0m")
                #if choix == "5":


            else:
                print("\n\n💤💤💤 Fin du programme 💤💤💤")
                break

                #if choix == "000":
