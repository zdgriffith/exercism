def abbreviate(phrase):

    letters = 0
    acronym = ''
    for c in phrase:
        if c.isalpha():
            if letters == 0:
                acronym += c.upper()
            letters += 1
        else:
            letters = 0
        
    return acronym
