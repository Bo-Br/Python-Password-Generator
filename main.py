from modules.analyze import analyze
from modules.database_manager import db_add, db_erase, db_read, db_update
from modules.generate import generate_p
#from modules.search import search
from modules.stat import stats, listing
from datetime import date


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
    choix = input("\nPlease select an option (1-7):  \n")
        
         
    if choix == "1":
                while True:
                        try:
                                length = int(input("\nChoose your password length: (8-64)"))
                                if length < 8 or length > 64:
                                        raise ValueError
                                break
                        except ValueError:
                                print("Error: please enter a number between 8 and 64.")

                print("\nChoose your password composition?")

                while True:
                        try:
                                num = int(input("\nDo you want numbers? (yes = 1, no = 0): "))
                                if num not in (0, 1):
                                        raise ValueError
                                break
                        except ValueError:
                                print("Error: please enter 1 or 0.")

                while True:
                        try:
                                let = int(input("\nDo you want letters? (yes = 1, no = 0): "))
                                if let not in (0, 1):
                                        raise ValueError
                                break
                        except ValueError:
                                print("Error: please enter 1 or 0.")

                while True:
                        try:
                                spe_c = int(input("\nDo you want special_characters? (yes = 1, no = 0): "))
                                if spe_c not in (0, 1):
                                        raise ValueError
                                break
                        except ValueError:
                                print("Error: please enter 1 or 0.")

                inp_psd = 0

                while inp_psd != 1:
                        passwrd = generate_p(length, num, let, spe_c)
                        try:
                                inp_psd = int(input(f"\nDo you like the password : {passwrd} ? (1/0) : "))
                                if inp_psd not in (0, 1):
                                        raise ValueError
                        except ValueError:
                                print("Error: please enter 1 or 0.")


    elif choix == "2":
            print("\n Analyze your password: ")
            mdp = input("\n Enter your password: ")
            print(f"The score of your password is: {analyze(mdp)}")
            
            
            
    elif choix == "3":
            print("\nAdd a new account") 
            
            site = input("\nWebsite name : ") 
            categorie = input("\nCategory : ") 
            email = input("\nEmail : ")
            mdp = input("\nPassword : ")
            
            ID = { "site": site, 
                   "categorie": categorie,
                   "email": email,
                   "mdp": mdp,
                   "date_creation": str(date.today()),
                   "score": analyze(mdp) }
            db_add(ID)
            
            print("\nAccount successfully added!\n")

            
            
    elif choix == "4":
            print("\nList All Accounts")
            listing()



    elif choix == "5":
            print("\nSearch account")
            name = int(input("\nSearch by : Website, Category, Email, Password: "))
            #search(name) 



    elif choix == "6":
            print("\nView statistics")
            stats()



    elif choix == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please choose between 1 and 7.")
