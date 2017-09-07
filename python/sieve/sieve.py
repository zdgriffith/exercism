def sieve(max_number):
    numbers = range(2,max_number+1,1)
    primes  = []

    for i in numbers:
        primes.append(i)
        mult = 2 
        while (i*mult) <= max_number:
            if i*mult in numbers:
                numbers.remove(i*mult)
            mult += 1

    return primes
