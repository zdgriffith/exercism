def distance(dna1, dna2):
    if len(dna1) != len(dna2):
        raise ValueError('DNA sequences not equal, Hamming distance undefined')

    hamming = 0
    for i, char in enumerate(dna1):
        if char != dna2[i]:
            hamming += 1

    return hamming
