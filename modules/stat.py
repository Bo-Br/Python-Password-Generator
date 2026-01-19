from database_manager import db_read
from datetime import datetime, timedelta
from search import db_print

def stats():
    """
    Gives statistics for the whole database.

    The function:
    - Reads the database using db_read()
    - Counts the total number of passwords
    - Calculates the average password strength score
    - Lists sites with passwords older than 90 days

    Expected database format:
    {
        "ID": {
            "site": "example.com",
            "date_creation": "YYYY-MM-DD",
            "score": <int>
        }
    }

    Returns:
        None
    """
    try:
        database = db_read()
        database_score = 0

        today = datetime.today()
        old_limit = today - timedelta(days=90)

        old_passwords = []

        print(f"There is {len(database.keys())} password(s) in the database")

        for i in database.values():
            database_score += int(i["score"])

            creation_date = datetime.strptime(i["date_creation"], "%Y-%m-%d")
            if creation_date < old_limit:
                old_passwords.append(i["site"])

        print(f"the average score of your passwords is {str(database_score / len(database.keys()))[:3]}")
        print(f"Passwords older than 90 days: {len(old_passwords)}")
        if old_passwords:
            print("Old password sites:")
            for site in old_passwords:
                print(f"- {site}")

    except ZeroDivisionError:
        print("Database is empty, cannot calculate statistics")

    except KeyError as e:
        print(f"Missing expected key in database entry: {e}")

    except ValueError:
        print("Invalid date or score value detected in database")

    except Exception as e:
        print(f"Unexpected error while computing stats: {e}")


def listing():
    """
    Lists all the elements of the database with their ID.

    The function:
    - Reads the database using db_read()
    - Prints each ID and its associated fields

    Expected database format:
    {
        "ID": {
            "field": "value",
            ...
        }
    }

    Returns:
        None
    """
    try:
        database_1 = db_read()
        db_print(database_1)

    except Exception as e:
        print(f"Unexpected error while listing database: {e}")








