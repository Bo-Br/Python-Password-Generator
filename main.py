from modules import add, analyse, database_manager, generate, search, stat


def afficher_menu():
    print("\n            MENU: ")
    print(" =========================== ")
    print("\n 1. Génerer un mot de passe")
    print("\n 2. Analyser un mot de passe")
    print("\n 3. Ajouter un compte")
    print("\n 4. Lister tous les comptes")
    print("\n 5. Rechercher un compte")
    print("\n 6. Staristique ")
    print("\n 7. Quitter")
    print("\n =========================== \n")


while True:
    afficher_menu()
    choix = input("Faite votre choix entre (1-7).")
        
         
    if choix == "1":
            generate()
    elif choix == "2":
            analyse()
    elif choix == "3":
            db_add()
    elif choix == "4":
            db_list()
    elif choix == "5":
            dn_research()
    elif choix == "6":
            db_statistics()
    elif choix == "7":
         print("Au revoir !")
else:
    print("Option invalide. Veuillez choirir une option entre 1 et 7.")