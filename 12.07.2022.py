# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 19:03:29 2022

@author: andrz
"""
#Exercise1

#helloMessage = "Hello %s"

#print(helloMessage % ('Kate'))
#print(helloMessage % ('Chris'))

#Exercise2

#helloMessage = "Hello {0:s} !"

#print(helloMessage.format('Kate'))
#print(helloMessage.format('Chris'))

#Exercise3

#helloMessage = "% has %d %s"

#print(helloMessage % ('Kate', 1,'animal'))
#print(helloMessage % ('Chris', 100000, '$'))

#Exercise4

helloMessage = "{0:s} has {1:d} {2:s}"

print(helloMessage.format('Kate', 1,'animal'))
print(helloMessage.format('Chris', 100000, '$'))

#Exercise5

line = "{0:20s} costs {1:6d} €"

print(line.format('ICE CREAM',10))
print(line.format('TRIP TO VENICE', 1200))
print(line.format('PIZZA HAWAI', 25))

name = "Andrzej"
age = 29
daysInYear = 365
#message = "%s is %d years old, so is about %d days old"
#print(message % (name,age,age*daysInYear))

message = "{0:s} is {1:d} years old, so is about {2:d} days old"
print(message.format(name,age,age*daysInYear))

#Exercise6

print('1234567890 divided by 12345 is', 1234567890//12345, 'and the rest is', 1234567890%12345)

