from database_manager import db_read
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
    for db_keys, db_value in db_copy.items():
        for i in db_keys:
            if db_copy[i][category] == name:
                to_return += [i]
        if not to_return:
            print("Error, please retry.")
            return None
        else:
            return to_return

            
        

