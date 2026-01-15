from modules import add, analyze, database_manager, generate, search, stat


def afficher_menu():
    print("\n            MENU: ")
    print(" =========================== ")
    print("\n 1. Generate Password")
    print("\n 2. Analyze Password")
    print("\n 3. Add Account")
    print("\n 4. List All Accounts")
    print("\n 5. Search Account")
    print("\n 6. Statistics ")
    print("\n 7. Exit Program")
    print("\n =========================== \n")


while True:
    afficher_menu()
    choix = input("Please select an option (1-7): ")
        
         
    if choix == "1":
            generate()
    elif choix == "2":
            analyze()
    elif choix == "3":
            db_add()
    elif choix == "4":
            db_list()
    elif choix == "5":
            dn_research()
    elif choix == "6":
            db_statistics()
    elif choix == "7":
         print("Goodbye!")
else:
    print("Invalid option. Please choose between 1 and 7.")
