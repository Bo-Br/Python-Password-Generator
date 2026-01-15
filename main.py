from modules.generate import generate_p


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
        length = int(input("Choose your password length: (8-64)"))
        
        print("Choose your password composition?")
        num = int(input("Do you want numbers? (yes = 1, no = 0): "))
        let = int(input("Do you want letters? (yes = 1, no = 0): "))
        spe_c = int(input("Do you want special_characters? (yes = 1, no = 0): "))
        
        inp_psd = 0
        
        while inp_psd != 1:
            
            passwrd =  generate_p(length, num, let, spe_c)
            inp_psd = int(input(f"Do you like the password : {passwrd} ? (1/0) : "))
            if inp_psd == 1:
                pass


    """
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
    """
