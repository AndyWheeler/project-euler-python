# -*- coding: utf-8 -*-
# Project Euler - Problem 11 - Largest product in a grid
# solution by capntimb (Andy Wheeler)
#
#"In the 20×20 grid below, four numbers along a diagonal line have been marked in red.
#
#       [see problem11grid.txt]
#
# The product of these numbers is 26 × 63 × 78 × 14 = 1788696.
#
# What is the greatest product of four adjacent numbers in the same direction
# (up, down, left, right, or diagonally) in the 20×20 grid?"

###
# largestProduct takes a text file containing a 20x20 grid of digits
# and returns the largest product of four adjacent numbers

def largestProduct():
    #read file
    with open('/Users/Tommy/py/problem11grid.txt') as gridfile:
        grid = gridfile.read()
        gridfile.seek(0)
        print grid
        digits = []
        print gridfile
        for line in gridfile:
            digits.append(line)
        print digits
        
largestProduct()