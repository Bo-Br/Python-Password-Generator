from .database_manager import db_read


def db_print(db):
    """
    Prints the content of the database in a readable format.

    This function iterates through the database dictionary and
    prints each account ID along with its associated fields
    and values.

    Args:
        db: A dictionary representing the database content.

    Returns:
        None

    Raises:
        None
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
    Searches for an account in the database by category and value.

    This function searches through the database and looks for
    entries where the given category matches the provided value.
    If a match is found, the corresponding account is displayed.

    Args:
        category: The database field to search in (e.g. website, username).
        name: The value to search for in the selected category.

    Returns:
        None if no result is found, otherwise prints the matching account.

    Raises:
        KeyError: If the specified category does not exist in the database.
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

