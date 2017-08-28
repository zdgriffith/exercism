def rotate(phrase, key):
    letters = ['a','b','c','d','e','f',
               'g','h','i','j','k','l',
               'm','n','o','p','q','r',
               's', 't','u','v','w','x','y',
               'z']

    code = ''
    for c in phrase:
        if c.isalpha():
            index = letters.index(c.lower())+key
            if index > 25:
                index -= 26
            
            if c.isupper():
                code += letters[index].upper()
            else:
                code += letters[index]
        else:
            code += c
        
    return code
