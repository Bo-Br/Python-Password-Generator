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

    db_max = max([int(num) for num in db_copy.keys()])
    new_ID = str(db_max + 1)
    db_copy[new_ID] = Item
    with open(db_path, "w") as fichier:
        json.dump(db_copy, fichier, indent = 4) #indent sert a une meilleure lisibilité


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
    db_copy[ID][category] = Item
    with open(db_path, "w") as fichier:
        json.dump(db_copy, fichier, indent = 4) #indent sert a une meilleure lisibilité


def db_erase(ID):
    db_copy = db_read()
    db_path = search_path()
    del db_copy[ID]
    with open(db_path, "w") as fichier:
        json.dump(db_copy, fichier, indent = 4) #indent sert a une meilleure lisibilité

db_add({
            "site": "data",
            "categorie" : "data",
            "email" : "data",
            "mdp" : "data", 
            "date_creation" : "data",
            "score" : "data"
        })

print(db_read())

db_erase("7")
db_erase("8")

print(db_read())