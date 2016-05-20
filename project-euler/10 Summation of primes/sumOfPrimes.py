##find the sum of all primes below the provided limit
def sumOfPrimes(limit):
    #prime list (pun intended)
    primes = []
    for i in range(limit+1):
        primes.append(True)
    primes[0] = False
    primes[1] = False
    #sieve away
    for n in range(2, int(limit**(0.5))+1):
        if primes[n] is True:
            m = n**2
            while m <= limit:
                primes[m] = False
                m += n
    #all primes within limit found; sum them all!
    total = 0
    for i in range(limit):
        p = primes[i]
        if p == True:
            print "%i is prime" % i
            total += i
    return total
    
print sumOfPrimes(2000000)