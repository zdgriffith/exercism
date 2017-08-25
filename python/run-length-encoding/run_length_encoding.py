def decode(code):
    phrase       = ''
    skip_repeats = False
    for i, c in enumerate(code):

        if c.isalpha() or c.isspace():
            skip_repeats = False
            if i == 0 or not code[i-1].isdigit():
                phrase += c
    
        if c.isdigit():
            if skip_repeats == True:
                continue
            else:
                places = 1
                while code[i+places].isdigit():
                    places += 1
                phrase += int(code[i:i+places])*code[i+places]
                skip_repeats = True

    return phrase

def encode(phrase):

    count = -1
    code  = ''
    last  = len(phrase)
    for i, c in enumerate(phrase):
        if count == -1:
            count  = 1
        elif c == phrase[i-1]:
            count += 1
        else:
            if count == 1:
                code  += phrase[i-1]
            else:
                code  += str(count) + phrase[i-1]
            count  = 1

        if i == last - 1:
            if count == 1:
                code  += phrase[i]
            else:
                code  += str(count) + phrase[i]

    return code
