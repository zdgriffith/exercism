def square_of_sum(number):
    tot = 0
    for n in range(number):
        tot += n+1
        
    return tot**2

def sum_of_squares(number):
    tot = 0
    for n in range(number):
        tot += (n+1)**2

    return tot

def difference(number):
    return square_of_sum(number) - sum_of_squares(number)
