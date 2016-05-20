debug = False

def sum_multiples(limit, multiples):
    total = 0
    for number in range(limit):
        factor = False
        for m in multiples:
            if number%m == 0:
                factor = True
        if factor:
            total += number
    return total

print sum_multiples(1000 ,[3, 5])
