letters = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "m", "n",
           "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y","z","A","B",
           "C", "D", "E", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q",
           "R", "S", "T", "U", "V", "W", "X", "Y", "Z")

numbers = ("2", "3", "4", "5", "6", "7", "8", "9")

special_character = ("!", "#", "$", "%", "&", "*", "+", "-", "=", "?", "@", "^", "_")

def analyze (password):
    
    score = 5
    test_s = 0 
    test_l = 0
    test_n = 0
    

    
    for letter in password:
        if letter in letters:
            test_l = 1
        elif letter in numbers:
            test_n = 1
        else:
            test_s = 1
    if len(password) < 12:
        score = 3
    if test_n == 0:
        score = score - 2
        
    if test_l == 0:
        score = score -2
    
    if test_s == 0:
        score = score - 1
        
    if len(password) > 16 and score == 5:
        score = 6
    
    if len(password) < 8:
        score = 0
    
    return score
