def word_count(phrase):

    spaced_phrase = ''
    for c in phrase:
        if c.isalnum():
            spaced_phrase += c.lower()
        else:
            spaced_phrase += ' '

    words = {}
    for word in spaced_phrase.split():
        if word not in words.keys():
            words[word] = 1
        else:
            words[word] += 1            
    return words
