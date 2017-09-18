import numpy as np

def sum_of_multiples(n_max, mult_list):

    total = 0
    for i in range(n_max):
        if np.any([i%mult == 0 for mult in mult_list]):
            total += i

    return total
