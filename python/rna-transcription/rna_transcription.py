def to_rna(dna):
    dna_to_rna = {'G':'C','C':'G','T':'A','A':'U'}
    rna = ''
    for char in dna:
        if char not in dna_to_rna.keys():
            #Wouldn't a sys.exit statement make more sense here? That doesn't pass the tests though...
            print('%s is not a valid DNA strand! Returning empty string.' % char)
            return ''
        rna += dna_to_rna[char]
    return rna
