#liste_utilisateurs = [
    #     ["SEBASTIEN", 35, "Azerty12#", "Faible"],
    #     ["ARTHUR", 18, "Azerty12#f", "Moyen"],
    #     ["CORENTIN", 65, "Azerty12#f", "Moyen"],
    #     ["GABRIELLE", 42, "Azerty12#", "Faible"],
    #     ["THIERRY", 89, "Azerty12#ert", "Fort"],
    #     ["WILLO", 31, "Azerty12#f", "Moyen"],
    #     ["FABIENNE", 52, "Azerty12#f", "Moyen"],
    #     ["HECTOR", 26, "Azerty12#f", "Moyen"],
    #     ["JEREMIE", 37, "Azerty12#ert", "Fort"],
    #     ["EMILIE", 79, "Azerty12#", "Faible"],
    #     ["ISABELLE", 43, "Azerty12#ert", "Fort"],
    #     ["NATHALIE", 30, "Azerty12#f", "Moyen"],
    #     ["PATRICIA", 38, "Azerty12#ert", "Fort"],
    # ]

def ajouter_utilisateur(liste_utilisateurs, prenom, age):
    liste_utilisateurs.append({"prenom": prenom, "age": age})



liste_utilisateurs = []
liste_utilisateurs.append({"prenom": "SEBASTIEN", "age": 35})
print(f"Prénom => {liste_utilisateurs[0]['prenom']}, age => {liste_utilisateurs[0]['age']} ans")
liste_utilisateurs[0]['prenom'] = "CHARLES"
for utilisateur in liste_utilisateurs:
    print(f"{utilisateur['age']}")
prenom = "Pierre"
age = 45
utilisateur = {"prenom": prenom, "age": age}
liste_utilisateurs.append(utilisateur)
print(liste_utilisateurs)