from datetime import date

from modules.analyze import analyze
from modules.database_manager import db_add, db_erase, db_read, db_update
from modules.generate import generate_p
from modules.search import search
from modules.stat import stats, listing



def afficher_menu():
    print("\n            MENU: ")
    print(" =========================== ")
    print("\n 1. Generate Password")
    print("\n 2. Analyze Password")
    print("\n 3. Add Account")
    print("\n 4. Delete Account")
    print("\n 5. List All Accounts")
    print("\n 6. Search Account")
    print("\n 7. Statistics ")
    print("\n 8. Exit Program")
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

                print("\nChoose your password composition")

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
                                inp_psd = int(input(f"\nDo you want to save the password : {passwrd} ? (yes = 1, no = 0): "))
                                if inp_psd == 1:
                                       db_copy = db_read()
                                       listing()
                                       user_choice = str(input("Choose the ID of the site to put the password in :"))
                                       if user_choice in db_copy.keys():
                                              db_update("password", passwrd, user_choice)
                                              db_update("date_created", str(date.today()), user_choice)
                                       else:
                                              print("ID inexistant")

                                elif inp_psd not in (0, 1):
                                        raise ValueError
                                
                                elif inp_psd == 0:
                                       break
                                
                                
                                
                        except ValueError:
                                print("Error: please enter 1 or 0.")


    elif choix == "2":
            print("\n Analyze your password: ")
            mdp = input("\n Enter your password: ")
            print(f"The score of your password is: {analyze(mdp)}")
            
            
            
    elif choix == "3":
            print("\nAdd a new account") 
            
            site = input("\nWebsite name: ") 
            categorie = input("\nCategory (mail, shop, social, other): ") 
            username = input("\nUsername: ")
            mdp = input("\nPassword: ")
            
            ID = { "website": site, 
                   "category": categorie,
                   "username": username,
                   "password": mdp,
                   "date_created": str(date.today()),
                   "score": analyze(mdp) }
            db_add(ID)
            
            print("\nAccount successfully added!\n")

    elif choix == "4":   
           listing()
           id_to_erase = input("\nChoose an ID to erase: ")
           db_erase(id_to_erase)  
            
    elif choix == "5":
            print("\nList All Accounts")
            listing()



    elif choix == "6":
            print("\nSearch account")
            categories = ("website", "category", "username", "password")
            category = ""
            while category not in categories:
                category = (input("\nSearch by : website, category, username, password: "))
                name = (input(f"Enter the word to search in the {category} category: "))
                if category not in categories:
                       print("Category error, retry.")
            search(category, name)



    elif choix == "7":
            print("\nView statistics")
            stats()



    elif choix == "8":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please choose between 1 and 8.")
