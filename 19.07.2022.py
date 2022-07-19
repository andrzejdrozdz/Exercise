# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 17:11:22 2022

@author: andrz
"""

data = ['Error:File cannot be open',
        'Error:No free space on disk',
        'Error:File missing',
        'Warning:Internet connection lost',
        'Error:Access denied']

for s in data:
    print(s.upper())

print('----------------------------------------------------------------------')
###############################################################################

for s in data:
    elements = s.split(':')
    print(elements[0].upper())
    print(elements[1])
    
print('----------------------------------------------------------------------')
###############################################################################

for s in data:
    elements1 = s.split(':')
    if elements1[0] == 'ERROR':
        print(elements1[1].upper())
    else:
        print(elements1[1])
