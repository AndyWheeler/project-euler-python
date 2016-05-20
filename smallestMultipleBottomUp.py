import primeFactors

def primePower(num):
    factors = primeFactors.primeFactorsOf(num)
    print "prime factors of " + str(num) + ": " + str(factors)
    return not factors or factors.count(factors[0]) == len(factors)

def smallestMultiple(upperBound):
    lim = upperBound
    powers = [1]
    for n in range(1, lim+1):
        #check to see if it's a prime power, aka if its prime factors are all equal
        #and also remove any lower power of that prime
        #TODO: explore starting at the top and working down. then it could just check
        #to see if the one it's trying divides evenly an element of the list
        power = primePower(n)
        if  power > 0:
            powers.append(n)
            if power > 1:
                base = n
                for p in range(1, power+1):
                    base = base/n
                powers.remove(base**(power-1))
    print powers
    #multiply all the prime powers
    product = 1
    for p in powers:
        product *= p
    return product
   
n = 4
#print primeFactors.primeFactorsOf(n)
#print primePower(n)
print smallestMultiple(10)