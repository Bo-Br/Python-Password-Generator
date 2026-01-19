from .database_manager import db_read


def db_print(db):
    """
    Docstring for db_print
    
    :param db: Description
    """
    if db:
        for db_id in db.keys():
                print(f"{db_id} : ")
                for db_key, db_value in db[db_id].items():
                    print(f"{db_key} : {db_value}")
    else:
        print("Error, database Empty")

def search(category, name):
    """
    Description:
    searches in the category by name of the category
    
    Parameters
    - category: Description
    - name: Description
    """
    db_copy = db_read()
    to_return = []
    for db_keys in db_copy.keys():
        if db_copy[db_keys][category] == name:
            to_return += [db_keys]
    if not to_return:
        print("Error, please retry.")
        return None
    else:
        db_print({str(to_return[0]) : (db_copy[str(to_return[0])])})


search("website", "cookie.io")