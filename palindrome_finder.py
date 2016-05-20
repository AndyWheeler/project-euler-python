import time

def checkPalindromity(num):
    num = str(num)
    half = len(num)/2
    front = num[0:half]
    back = num[half:]
    #print "front: " + front + " back:" + back
    for i in range(half):
        if front[i] != back[-i-1]:
            print num + " is not a palindrome - " + front[i] + " is not " + back[-i-1] + "\n"
            return False
    else:
        print num + " is a palindrome" + "\n"
        return True
        
def largestPalindrome(top):
    startTime = time.time();
    largest = 1
    checkingNextCol = False
    for col in range(top, 0, -1):
        
        if checkingNextCol:
            depth = top//col
        else:
            depth = col-1
            
        for row in range(top, depth, -1):
            print str(row) + " " + str(col) + " (" + str(largest) + ")" + ": "
            product = row*col
            if checkPalindromity(product) and product > largest:
                print "Found largest: " + str(product)
                largest = product
                if top-row > (top//col)+1:
                    print "in upper area; checking next col"
                    checkingNextCol = True
                    break
        if depth == top//col:
            break
    totalTime = time.time()-startTime
    print "Found solution in " + str(totalTime) + "s"
    return largest
    
