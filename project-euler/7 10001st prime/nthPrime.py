import time

def nthPrime(n):
    primes = [2]
    i = 2
    while len(primes) < n:
        #check if i has a previously-found prime as a factor
        #aka for each 
        for p in primes:
            if i%p == 0:
                break
        else:
            primes.append(i)         
        i += 1
    return primes[-1]
    
def nthPrimeTimed(n):
    startTime = time.time()
    primes = nthPrime(n)
    totalTime = time.time()-startTime
    print "Found solution in " + str(totalTime) + "s "
    return primes
    
print nthPrimeTimed(100001)