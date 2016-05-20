debug = False

def sum_even_fib(limit):
    total = 0
    term1 = 1
    term2 = 1
    while term2 < limit:
        if debug:
            print "term1: %d, term2: %d" % (term1, term2)
        #check term for evenness
        if term2%2 == 0:
            total += term2
            if debug:
                print "--found even term: %d. total: %d" % (term2, total)
        #generate next term
        term2 += term1
        term1 = term2 - term1
    return total

print sum_even_fib(4000000)
