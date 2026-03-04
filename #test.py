liste_utilisateurs = [
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
test = "e"
for i in liste_utilisateurs:
    if test.upper() in i[0]:
        print("oui")
    else:
        print("non")