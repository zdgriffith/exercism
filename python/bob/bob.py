import numpy as np

def hey(phrase):
    caps = [c.isupper() for c in phrase if c.isalpha()]

    truncator  = ''
    new_phrase = ''
    for c in phrase:
        truncator += c
        if not c.isspace():
            new_phrase += truncator
            truncator   = ''

    if len(caps)>0 and np.all(caps):
        return('Whoa, chill out!')
    elif len(new_phrase) == 0:
        return('Fine. Be that way!')
    elif new_phrase[-1] == '?':
        return('Sure.')
    else:
        return('Whatever.')
