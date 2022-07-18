# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 16:26:27 2022

@author: andrz
"""
'''
firstRow = 1
lastRow = 31
currentRow = firstRow
while currentRow <= lastRow:
    print('Row number', currentRow)
    currentRow +=1
'''
###############################################################################
'''
start = 1
end = 13
number = start
while number <= end:
    print(number, number*number, number*number*number)
    number+=1
'''

###############################################################################
'''
start = 0
end = 16
x = start
while x <= end:
    print(x, 2**x)
    x+=1
'''
###############################################################################
'''
numbers = [8,18,2,4,16,5,25,4,22,3,3,5,3,9,81,11]

i=0
max = len(numbers)-1
while i< max:
    print(i, numbers[i], numbers[i+1])
    if numbers[i]**2 == numbers[i+1]:
        print("\tFOUND!")
    i+=1
print('----------------------------------------------------------------------')
'''
###############################################################################
'''
numbers = [8,18,2,4,16,5,25,4,22,3,3,5,3,9,81,11]

i=0
max = len(numbers)-2
while i< max:
    print(i, numbers[i], numbers[i+1], numbers[i+2])
    if numbers[i]**2 == numbers[i+1] and numbers[i+1]**2 == numbers[i+2]:
        print("\tFOUND!")
    i+=1
print('----------------------------------------------------------------------')
'''

###############################################################################
'''
texts = ['zero','one','two','three','four','five','six','seven','eight','nine']

i=0
max = len(texts)-1
while i< max:
    print(i, texts[i], texts[i+1])
    if len(texts[i]) == len(texts[i+1]):
        print("\tFOUND!")
    i+=1
print('----------------------------------------------------------------------')
'''
###############################################################################
'''
Year = 18
myYear = 9

if myYear >= Year:
    print('Mogę prowadzić auto!')
else:
    print('Nie mogę prowadzić auta!')
'''
###############################################################################
'''
Year = 18
myYear = 9
drunk = False
if myYear >= Year and not drunk:
    print('Mogę prowadzić auto!')
elif drunk:
    print('Nie mogę prowadzić auta, jestem pijany!')
else:
    print('Nie mogę prowadzić jestem za młody!')
'''
###############################################################################
'''
number = 1
previousNumber = 0

while number <= 50:
    print(number + previousNumber)
    previousNumber = number
    number += 1
'''

###############################################################################
import random
my_number = random.randint(0,20)

guess = 1 

print('Guess my number!')

while guess != my_number:
    guess = int(input())
    if guess == my_number:
        print('You are right! It was:', my_number)
    elif guess > my_number:
        print('SSorry- my number is smaller than', guess, "Try again!")
    else:
        print('Sorry- my number is greater than', guess, 'Try again!')























