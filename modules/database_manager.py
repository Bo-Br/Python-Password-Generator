import json
import os


def search_path():
    """
    Returns the absolute path to the JSON database file.

    The function determines the directory of the current file,
    moves one level up to the project root, and builds the path
    to 'database/DB.json'.

    Returns:
        str: Absolute path to the database file.

    Raises:
        FileNotFoundError: If the database directory or file does not exist.
    """
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))  # takes the current directory name
        project_dir = os.path.dirname(base_dir)  # takes the previous directory name of base_dir
        db_path = os.path.join(project_dir, "database", "DB.json")  # finds the path to the .json database
        return db_path
    
    except Exception as e:
        raise FileNotFoundError("Unable to determine database path") from e


def db_read():
    """
    Reads and returns the content of the JSON database.

    Expected database structure:
    {
        "dataindex": {
            "site": "data",
            "categorie": "data",
            "email": "data",
            "mdp": "data",
            "date_creation": "data",
            "score": "data"
        }
    }

    Returns:
        dict: JSON content of the database.

    Raises:
        FileNotFoundError: If the database file cannot be found.
        json.JSONDecodeError: If the database file contains invalid JSON.
        IOError: If the file cannot be read.
    """
    db_path = search_path()
    try:
        with open(db_path, "r") as fichier:
            data = json.load(fichier)
            return data
        
    except FileNotFoundError:
        raise FileNotFoundError("Database file not found")
    
    except json.JSONDecodeError:
        raise ValueError("Database file contains invalid JSON")
    
    except Exception as e:
        raise IOError("Error while reading the database") from e


def db_add(Item):
    """
    Adds a new item to the database with an auto-incremented ID.

    Item structure:
    {
        "site": "data",
        "categorie": "data",
        "email": "data",
        "mdp": "data",
        "date_creation": "data",
        "score": "data"
    }

    Args:
        Item (dict): Data to be added to the database.

    Raises:
        ValueError: If database IDs are not numeric.
        IOError: If the database file cannot be written.
    """
    try:
        db_copy = db_read()
        db_path = search_path()

        db_max = max([int(num) for num in db_copy.keys()])  # Gives the maximum element in the keys list
        new_ID = str(db_max + 1)  # gives the new ID that goes after the greater ID
        db_copy[new_ID] = Item

        with open(db_path, "w") as fichier:
            json.dump(db_copy, fichier, indent=4)  # indent for better visibility

    except ValueError:
        raise ValueError("Database keys must be numeric strings")
    
    except Exception as e:
        raise IOError("Error while adding data to the database") from e


def db_update(category: str, Item: dict, ID: str):
    """
    Updates a specific category of an existing database entry.

    Update format:
    {
        "ID": {
            "category": "data"
        }
    }

    Args:
        category (str): The category to update.
        Item (dict): New data to assign to the category.
        ID (str): Database entry ID.

    Raises:
        KeyError: If the ID or category does not exist.
        IOError: If the database file cannot be written.
    """
    try:
        db_copy = db_read()
        db_path = search_path()

        db_copy[ID][category] = Item  # Changes the Item in the category at the ID

        with open(db_path, "w") as fichier:
            json.dump(db_copy, fichier, indent=4)  # indent for better visibility
    except KeyError:
        raise KeyError("Invalid ID or category")
    
    except Exception as e:
        raise IOError("Error while updating the database") from e


def db_erase(ID):
    """
    Erase the ID element in the json file.
    
    :param ID: A str or int ID to erase in the database.
    """
    ID = str(ID) #To avoid mistakes
    db_copy = db_read()
    db_path = search_path()
    
    if ID in db_copy:
        del db_copy[ID]
        with open(db_path, "w") as fichier:
            json.dump(db_copy, fichier, indent = 4) #indent for better visibility
    else: 
        print(f"Error : ID-{ID} not in database")
