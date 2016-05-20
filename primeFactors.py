def primeFactorsOf(num):
    if num == 1:
        return [1]
    factors = []
    primes = [2]
    while(num>1):
        #find lowest prime factor, pop it off, add it to list, repeat until you've found 'em all
        #try each prime in list, starting at the bottom
        for p in primes:
            if num%p == 0:
                factors.append(p)
                num = num/p
                break
        #if nothing in list is found, find next biggest prime and try it
        else:
            candidate = primes[-1]+1
            while candidate <= num:
                #see if a known prime is a factor
                for p in primes:
                    #if a factor is found
                    if candidate%p == 0:
                        #it's not prime; try next one
                        candidate += 1
                        break
                #if none are, it's prime; add to list and test it
                else:
                    primes.append(candidate);
                    if num%candidate == 0:
                        factors.append(candidate)
                        num = num/candidate
                    break
    return factors

n = 112
print "Prime factors of " + str(n) + ": " + str(primeFactorsOf(n))