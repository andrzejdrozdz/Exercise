# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 18:36:48 2022

@author: andrz
"""
#Excercise1
hitsTitle = ['BROTHER IN ARMS', 'BOHEMIAN RHAAPSODY', 'STAIRWAY TO HEAVEN', 'RIDERS ON THE STORM', 'WISH YOU WERE HERE']
print(hitsTitle)

hitsTitle.append('CHILD IN TIME')
hitsTitle.append('AGAIN')
print(hitsTitle)

hitsTitle.insert(2, 'HOTEL CALIFORNIA')
print(hitsTitle)

hitsTitle.insert(0, 'SOUND OF SILENCE')
print(hitsTitle)

print(hitsTitle.index('HOTEL CALIFORNIA'))

hitsTitle.remove('HOTEL CALIFORNIA')
print(hitsTitle)

hitsTitle[0]= ('ENJOY THE SILENCE')
print(hitsTitle)

hitsToRead = hitsTitle.copy()
print(hitsToRead)

hitsToRead.reverse()
print(hitsToRead)

hitsToRead.sort()
print(hitsToRead)


print(hitsToRead.pop(0))
print(hitsToRead.pop(0))
print(hitsToRead)

additionalSongs = ['WHISH YOU WERE HERE', 'RIDERS ON THE STORM']
print(additionalSongs)

hitsToRead.extend(additionalSongs)
print(hitsToRead)

print(hitsToRead.count('WHISH YOU WERE HERE'))
print(hitsToRead.count('RIDERS ON THE STORM'))

hitsToRead.clear()
print(hitsToRead)

#Excercise2

marketing = ['loyallity program', 'client promotion', 'market research']
marketing.append('public relations')
print(marketing)
print(marketing[3])

marketing.insert(2, 'investor relations')
print(marketing)

emailMarketing = marketing.copy()

emailMarketing.sort()
print(emailMarketing)

internalEmails = ['internal commucication']

emailMarketing.extend(internalEmails)
print(emailMarketing)

emailtuple = tuple(emailMarketing)

print(emailtuple)

#Excercise3

chanels = {'Google':1480, 'Email':300, 'Natural TRaffic':440, 'Tv Sport':700}
print(chanels)
print(chanels['Email'])

chanelsUpdate = {'Natural Traffic':520, 'News':600}
chanels.update(chanelsUpdate)
print(chanels)

print(chanels.keys())
print(chanels.pop('Email'))
print(chanels)


