digitNames = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9: "nine", 0:"zero"}
tensNames = {1:"ten", 2:"twenty", 3:"thirty" ,4:"forty", 5:"fifty", 6:"sixty", 7:"seventy", 8:"eighty", 9:"ninety"}
teenNames = {1:"eleven", 2:"twelve", 3:"thirteen", 4:"fourteen", 5:"fifteen", 6:"sixteen", 7:"seventeen", 8:"eighteen", 9:"nineteen"}

# Translates numerals up to 1000 into words in compliance with British usage.
def writeOut(number):
    """writes out a numeral
    
    >>> writeOut(2)
    'two'
    >>> writeOut(10)
    'ten'
    >>> writeOut(11)
    'eleven'
    >>> writeOut(60)
    'sixty'
    >>> writeOut(66)
    'sixty-six'
    >>> writeOut(115)
    'one hundred and fifteen'
    >>> writeOut(142)
    'one hundred and forty-two'
    >>> writeOut(200)
    'two hundred'
    >>> writeOut(1000)
    'one thousand'
    >>> writeOut(0)
    'zero'
    """
    
    writtenOut = ""
    number = str(number)
    place = len(number)
    if place == 0:
        return ""
    if int(number) == 0:
        return "zero"
    while place > 0:
        #print "writing " + number + "; place=" + str(place) + "\n"
        if int(number[0]) == 0:
            pass
        elif place == 4:
            writtenOut += "one thousand"
            if int(number[1:]) > 0:
                writtenOut += " "
        elif place == 3:
            writtenOut += digitNames[int(number[0])] + " hundred"
            if int(number[1]) != 0:
                writtenOut += " and "
            else:
                break
        elif place == 2:
            if int(number[0]) == 1 and int(number[-1]) > 0:
                writtenOut += teenNames[int(number[-1])]
                place -= 1
                number = number[1:]
            else:
                writtenOut += tensNames[int(number[0])]
                if int(number[1]) != 0:
                    writtenOut += "-"
        elif place == 1:
            writtenOut += digitNames[int(number[0])]
        place -= 1
        number = number[1:]
        #print "written " + writtenOut
    return writtenOut
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
