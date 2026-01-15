import json
import os


def search_path():
    """
    Searches the path of the database file and returns it
    """
    base_dir = os.path.dirname(os.path.abspath(__file__)) #takes the current directory name
    project_dir = os.path.dirname(base_dir) #takes the previous directory name of base_dir
    db_path = os.path.join(project_dir, "database", "DB.json") #finds the path to the .json database
    return db_path

def db_read():
    """
    Docstring for db_print
    returns the database in the form of 
    {
        "dataindex" : 
        {
            "site": "data",
            "categorie" : "data",
            "email" : "data",
            "mdp" : "data", 
            "date_creation" : "data",
            "score" : "data"
        }
    }
    """
    db_path = search_path()
    with open(db_path, "r") as fichier:
        data = json.load(fichier)
        return data

def db_add(Item):
    """
    Docstring for db_print
    Add the item to the database in the form of :
    {
        "ID" : 
        {
            "site": "data",
            "categorie" : "data",
            "email" : "data",
            "mdp" : "data", 
            "date_creation" : "data",
            "score" : "data"
        }
    }
    """

    db_copy = db_read()
    db_path = search_path()

    db_max = max([int(num) for num in db_copy.keys()]) #Gives the maximum element in the keys list
    new_ID = str(db_max + 1) #gives the new ID that goes after the greater ID
    db_copy[new_ID] = Item
    with open(db_path, "w") as fichier:
        json.dump(db_copy, fichier, indent = 4) #indent for better visibility


def db_update(category : str, Item : dict, ID : str):
    """
    Docstring for db_print
    Add the item to the categoy in the database ID in the form of :
    {
        "ID" : 
        {
            
            "category" : "data"

        }
    }
    """
    db_copy = db_read()
    db_path = search_path()
    db_copy[ID][category] = Item #Changes the Item in the category at the ID
    with open(db_path, "w") as fichier:
        json.dump(db_copy, fichier, indent = 4) #indent for better visibility


def db_erase(ID):
    """
    Erase the ID element in the json file.
    
    :param ID: A str or int ID to erase in the database.
    """
    ID = str(ID) #Pour eviter les erreurs
    db_copy = db_read()
    db_path = search_path()
    if ID in db_copy:
        del db_copy[ID]
        with open(db_path, "w") as fichier:
            json.dump(db_copy, fichier, indent = 4) #indent for better visibility
    else: 
        print(f"Error : ID-{ID} not in database")

