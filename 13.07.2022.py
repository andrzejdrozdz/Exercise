# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 17:21:13 2022

@author: andrz
"""
# Excercise1

isAutomaticMode = True
is80percentLight = True
isDirectLight = False
isRainy = False
turnLightsOn = isAutomaticMode and (
    not is80percentLight or isDirectLight or isRainy)

print("Automatic Mode :     ",isAutomaticMode)
print("Is the light good:   ",is80percentLight)
print("Is sun low:          ",isDirectLight)
print("Is it rainy:         ",isRainy)
print("TURN LIGHTS ON:      ",turnLightsOn)


# Excercise2

v1 = 126
v3 = 126.0
v2 = '126'
v4 = '126.0'

print(v1, type(v1))
print(v2, type(v2))
print(v3, type(v3))
print(v4, type(v4))
print(v1+v3, type(v1+v3))
print(v2+v4, type(v2+v4))
print(7-1*0+3+3)
print(99+9/9)

# Excercise2

q = "THE EYES"
print(q)
print(q[0],q[1],q[2],q[3],q[4],q[5],q[6])


q = 'a gentleman'
print(q)
print(q[3],q[6],q[7],q[2],q[0],q[4],q[5],q[1],q[8:])
print(q[3]+q[6]+q[7]+q[2]+q[0]+q[4]+q[5]+q[1]+q[8:])


q = "THE MORSE CODE"
# HERE COMES DOTS
print(q[1:3],q[6],q[8],q[3],q[10:12],q[4],q[13],q[9],q[12],q[5],q[0],q[7])
print(q[1:3]+q[6]+q[8]+q[3]+q[10:12]+q[4]+q[13]+q[9]+q[12]+q[5]+q[0]+q[7])



line = 'Program "Kropka nad i" nadamy o: 22:00'
time = line[ line.find(':')+2: ]
print(time)

tmp = line[ line.find('"')+1: ]
title = tmp [:tmp.find('"')]
print(title, time)


line = 'Program "Pytanie na sniadanie" nadamy o: 6:00'
time = line[ line.find(':')+2:]
print(time)
tmp = line[ line.find('"')+1:]
title = tmp[:tmp.find('"')]
print(title, time)


# Excercise3



shoesize = 45
number = (shoesize*5 +50)*20+1017 -1993
print('shoe size is:' ,number//100)
print('birth date is:' ,number %100)



x=107
print('this shold be 5:', (x*2+10)/2-x)
print('2+2*2=', 2+2*2)
print('7+7/7+7*7-7', 7+7/7+7*7-7)
presence = 0.85
note = 3.5
finalWorkOK = False
print('you need to be present and have good notes or do the final work', 
      presence >= 0.8 and note >=3 or finalWorkOK)
print('you need to be present and have good notes and do the final work', 
      presence >= 0.8 and note >=3 and finalWorkOK)




