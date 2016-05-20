import primeFactors

#primePower(num) returns True if num is a prime power, False otherwise
def primePower(num):
    factors = primeFactors.primeFactorsOf(num)
    #print "prime factors of " + str(num) + ": " + str(factors)
    isPrimePower = not factors or factors.count(factors[0]) == len(factors)
    return isPrimePower

def smallestMultiple(upperBound):
    lim = upperBound
    powers = []
    for n in range(lim, 1, -1):
        #check to see if it's a prime power, aka if its prime factors are all equal
        #check to see if it evenly divides an element of the list. if not, add to list
        isPower = primePower(n)
        if isPower:
            if powers:
                for p in powers:
                    if p%n == 0:
                        break
                else:
                    powers.append(n)
            else:
                powers.append(n)
    print powers
    #multiply all the prime powers
    product = 1
    for p in powers:
        product *= p
    return product
   
n = 16
#print primeFactors.primeFactorsOf(n)
#print primePower(n)
print smallestMultiple(14)