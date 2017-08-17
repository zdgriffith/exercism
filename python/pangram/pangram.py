def is_pangram(sentence):

    char_list = []
    
    unique_letters = 0
    for char in sentence.lower():
        if char.isalpha():
            if char not in char_list:
                unique_letters += 1
                char_list.append(char)

    if unique_letters == 26:
        return True
    else:
        return False
