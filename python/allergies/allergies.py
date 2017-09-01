class Allergies(object):

    def __init__(self, number):
        pairs = {1:  'eggs',
                 2:  'peanuts',
                 4:  'shellfish',
                 8:  'strawberries',
                 16: 'tomatoes',
                 32: 'chocolate',
                 64: 'pollen',
                 128:'cats'}
                
        codes = [128,64,32,16,8,4,2,1]

        while number >= 256:
            number -= 256

        self.allergies = []
        for code in codes:
            if code <= number:
                self.allergies.append(pairs[code])
                number -= code

    def is_allergic_to(self, string):
        
        if string in self.allergies:
            return True
        else:
            return False

    @property
    def lst(self):
        return self.allergies
