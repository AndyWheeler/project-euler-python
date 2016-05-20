def sumOfSquares(limit):
    total = 0
    for n in range(1, limit+1):
        total += n**2
    return total
    
def squareOfSums(limit):
    total = 0
    for n in range(1, limit+1):
        total += n
    return total**2

def sumSquareDifference(limit):
    return squareOfSums(limit) - sumOfSquares(limit)
    
n = 100
print sumOfSquares(n)
print squareOfSums(n)
print sumSquareDifference(n)