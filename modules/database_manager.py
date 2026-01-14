import json
import os 


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
    base_dir = os.path.dirname(os.path.abspath(__file__)) #takes the current directory name
    project_dir = os.path.dirname(base_dir) #takes the previous directory name
    db_path = os.path.join(project_dir, "database", "DB.json") #finds the path to the .json database
    with open(db_path, "r") as fichier:
        data = json.load(fichier)
        return data




