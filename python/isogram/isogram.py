def is_isogram(word):

    char_list = []

    for char in word.lower(): #make all letters lowercase to avoid mixed cases
        if char.isalpha(): #only care about letters in the phrase
            if char in char_list:
                return False
            else:
                char_list.append(char)
    return True 
