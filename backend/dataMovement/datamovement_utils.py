import re

def special_match(strg, search=re.compile(r'[^EWRX]').search):
    return not bool(search(strg))

def isValidMove(movement):
    isValid = False

    if len(movement) <= 4:
        isValid = special_match(movement)

    return isValid