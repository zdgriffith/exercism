def encode(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    passphrase = ''
    index      = 0 

    for i, c in enumerate(string.lower()):

        if c.isalpha():
            passphrase += alphabet[abs(alphabet.index(c)-25)]
            index += 1
        elif c.isdigit():
            passphrase += c
            index += 1
        else:
            continue

        if index == 5:
            passphrase += ' '
            index = 0 

    if passphrase[-1] == ' ':
        return passphrase[:-1]
    else:  
        return passphrase

def decode(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    original = ''
    for c in string.lower():
        if c.isalpha():
            original += alphabet[abs(alphabet.index(c)-25)]
        if c.isdigit():
            original += c
    return original 
