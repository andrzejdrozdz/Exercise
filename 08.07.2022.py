# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 17:10:05 2022

@author: andrz
"""

#Exercise1
print ('TVP1','TVP2', 'TVN', 'Polsat', 'BBC', 'HBO', 'MTV')


#Exercise2
print ('TVP1','TVP2', 'TVN', 'Polsat', 'BBC', 'HBO', 'MTV', sep=';')

#Exercise3
print ('TVP1','TVP2', 'TVN', 'Polsat', 'BBC', 'HBO', 'MTV', sep=' but better is ')

#Exercise4
ProgramName ='BBC'
Item = 'News'
Time = '18:00'

print ('I like Watching ', ProgramName,' at ', Item,' on ', Time,'.', sep='')

#Exercise4
print ('USA', 'FRA','POL', sep='\n')


#Exercise5
quote='A good programmer is someone who always looks both ways before crossing a one-way street'

print(quote.upper())
print(quote.lower())
print(quote.endswith('street'))
print(quote.isupper())
print(quote.upper().isupper())
print(quote.find('one'))
print(quote.replace('one','1'))
print(quote.replace('one','1').replace('both','2'))
print(quote.split(' '))
print(quote.isnumeric())
print(quote.isdecimal())
print(quote.isalpha())
print(quote.isalnum())

#Excercise6
firstName ='Kasia'
famillyName ='Sowa'
lastName ='Mrugała'
newName = firstName+ " "+famillyName+" "+lastName
print(newName)

#Excercise7
music = '"Uniwersal Fanfare" Jerry Goldsmith "Happy Together" Garry Bonner "I\'m a Man" Steve Wonder'
print(music)

#Excercise8
music = '"Uniwersal Fanfare" Jerry Goldsmith \n"Happy Together" Garry Bonner \n"I\'m a Man" Steve Wonder'
print(music)




