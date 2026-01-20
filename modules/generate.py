import secrets

# Définition des tuples de caractères sécurisés
letters = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "m", "n",
           "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y","z","A","B",
           "C", "D", "E", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q",
           "R", "S", "T", "U", "V", "W", "X", "Y", "Z")

numbers = ("2", "3", "4", "5", "6", "7", "8", "9")

special_character = ("!", "#", "$", "%", "&", "*", "+", "-", "=", "?", "@", "^", "_")

score_password = {
    "0" : "Porte ouverte",
    "1" : "Très mauvaise",
    "2" : "Mauvais",
    "3" : "Moyen",
    "4" : "Convenable",
    "5" : "Bon",
    "6" : "Très bon",
}



def generate_p (password_length, num, let, spe_c):
    
    pool = ()
    password = ""
    if num == 1:
        pool += numbers
    if let == 1: 
        pool += letters
    if spe_c == 1:
        pool += special_character
    for i in range(0 , password_length): 
        password += str(secrets.choice(pool))
    return password
    

