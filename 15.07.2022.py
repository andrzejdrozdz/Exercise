# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 17:35:41 2022

@author: andrz
"""
'''
MIN_LIKE = 500
MIN_SHARES = 100

num_like = 300
num_shares = 550

if num_like >= MIN_LIKE and num_shares >= MIN_SHARES:
    print('GREAT! Today our prizes drop 10% !!!')
else:
    print('We still need more likes and shares to start the promotion')
'''
###############################################################################
'''
isPizzaOrdered = True
isWeekend = False
isBigDrinkOrdered = True

if(isPizzaOrdered or isBigDrinkOrdered) and not isWeekend:
    print('Burger for FREE!!!')
else:
    print('Come to us on week day and consider buying Pizza or BigDrink to have Burger for free')
'''
###############################################################################

'''
diskSize = 140
diskSizeUsed = 133
fileSize = 10

if diskSize >= diskSizeUsed + fileSize:
    print('File Can be downloaded')
else:
    print("There isn't enough free disk space to download the file. Sorry :(')")
'''

###############################################################################
'''
MIN_LIKE = 500
MIN_SHARES = 100

num_like = 300
num_shares = 550

if num_like >= MIN_LIKE and num_shares >= MIN_SHARES:
    print('GREAT! Today our prizes drop 10% !!!')
else:
    if num_like < MIN_LIKE:
        print('We still need more likes to start the promotion')
    else:
        print('We still need more shares to start the promotion')
    
 ''' 
############################################################################### 
'''
MIN_LIKE = 500
MIN_SHARES = 100

num_like = 300
num_shares = 550

if num_like >= MIN_LIKE and num_shares >= MIN_SHARES:
    print('GREAT! Today our prizes drop 10% !!!')
elif num_like < MIN_LIKE:
    print('We still need more likes to start the promotion')
else:
    print('We still need more shares to start the promotion')
'''
############################################################################### 
'''

isPizzaOrdered = True
isWeekend = True
isBigDrinkOrdered = True

if(isPizzaOrdered or isBigDrinkOrdered) and not isWeekend:
    print('Burger for FREE!!!')
else:
    if isWeekend:
        print('Come to us on week day.')
    else:
        print('YOu need to order Pizza or Big drink to have a Burger coupon.')

'''

############################################################################### 
'''

isPizzaOrdered = True
isWeekend = True
isBigDrinkOrdered = True

if(isPizzaOrdered or isBigDrinkOrdered) and not isWeekend:
    print('Burger for FREE!!!')
elif isWeekend:
    print('Come to us on week day.')
else:
    print('YOu need to order Pizza or Big drink to have a Burger coupon.')

'''

############################################################################### 

'''

musclePain = False
fever = True
weakness = True

if musclePain and fever and weakness:
    print('Suspicion of influenza')
else:
    print('The flu is unlikely')
    
'''
###############################################################################

musclePain = False
fever = True
weakness = True

if musclePain and fever and weakness:
    print('Suspicion of influenza')
elif not (musclePain and fever) and weakness:
    print('Just take a rest!')
else:
    print('you may be cold')

isMan = True
if musclePain and fever and weakness or isMan and (musclePain or fever or weakness):
    print('Susppicion of influenza.')
elif not (musclePain and fever) and weakness:
    print('Just take a rest!')
else:
    print('This only cold.')
    

isCheckCompleted = True

print('CHECK IS COMPLETED' if isCheckCompleted else 'CHECK NOT DONE YET!')








