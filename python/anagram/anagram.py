import numpy as np
def detect_anagrams(string, array):
    matches = []
    string  = string.lower()
    for i, word in enumerate(array):
        word = word.lower()

        if word == string or len(word) != len(string):
            continue

        diff = 0
        for c in string:
            if c not in word:
                diff += 1 
            else:
                if np.sum([c==c_i for c_i in string]) != np.sum([c==w_i for w_i in word]):
                    diff += 1 
        if diff == 0:
            matches.append(array[i])

    return matches
