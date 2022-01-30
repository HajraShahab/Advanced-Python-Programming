#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 17:30:35 2020

@author: hajrashahab
"""

import re 

with open('pop.csv') as fin:
    states = []
    for line in fin:
        states.append(line) 
    print(states)
        
#1
print('1:')
pattern = 'Oregon'
for line in states:
    if re.search(pattern, line) != None:
        print(line)


#2
print('2:')
pattern = 'O'
for line in states:
    if re.search(pattern, line) != None:                          
        print(line)

#3
print('3:')
pattern = '[OP]'
for line in states:
    if re.search(pattern, line) != None:                          
        print(line)

#4
print('4:')
pattern = r'^1'
for line in states:
    if re.search(pattern, line) != None: 
        print(line)

#5
print('5:')
pattern = r'0$'
for line in states:
    if re.search(pattern, line) != None: 
        print(line)

#6
print('6:')
pattern = r'[S-Zs-z]'
for line in states:
    if re.search(pattern, line) != None: 
        print(line)

#7
print('7:')
pattern = r'00*'                                    
for line in states:
    if re.search(pattern, line) != None: 
        print(line)

#8
#this question is ambiguous. I have tried to resolve it two ways as the question doesnt state whether 
#we are supposed to follow the order once or should the order hold across all numerical values in statement
print('8:')
pattern = r'5.*4.*3.'                            
for line in states:
    if re.search(pattern, line) != None: 
        print(line)
        
print('8:')
pattern = r'5.*4.*3'                            
for line in states:
    if re.search(pattern, line) != None: 
        print(line)

#9
print('9:')                                                       
pattern = r'[A-Za-z] [A-Za-z]'                 
for line in states:
    if re.search(pattern, line) != None: 
        print(line)

#10
print('10:')
pattern = r'[iI].*[iI]'                              
for line in states:
    if re.search(pattern, line) != None: 
        print(line)
