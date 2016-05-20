import math

def is_square(apositiveint):
  x = apositiveint // 2
  seen = set([x])
  while x * x != apositiveint:
    x = (x + (apositiveint // x)) // 2
    if x in seen: return False
    seen.add(x)
  return True

def pythagoreanSum(total):
    foundIt = False
    a = 1
    b = 1
    while not foundIt:
        while a <= b:
            csquared = a**2+b**2
            c = math.sqrt(csquared)
            print "trying %d**2 + %d**2 = %d**2" % (a, b, c)
            if is_square(csquared) and a + b + c == 1000:
                print "%f + %f + %f == 1000" % (a, b, c)
                return a, b, c
            a += 1
        a = 1
        b += 1 
            
#for n in range(110, 130):
#    print n, is_square(n)

print pythagoreanSum(1000)