#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 11:51:30 2020

@author: hajrashahab
"""

import pandas as pd

allPop = pd.read_csv('nstData.csv')
print(allPop)

#2a
print('Q2a:\n')
print('First two lines of allPop:\n', allPop.head(2))
print('Last five lines of allPop:\n', allPop.tail(5))

#2b
print('Q2b:\n')
print('Statistics:\n', allPop.describe())
print('Statistics- ESTIMATESBASE2010:\n', allPop['ESTIMATESBASE2010'].describe()) 
print('ESTIMATESBASE2010_mean:\n', allPop['ESTIMATESBASE2010'].describe().loc['mean'])

#2c
print('Q2c:\n')
states = allPop ['NAME']
states = states[5:]
print(states)

#2d
print('Q2d:\n')
row_constraint = allPop["STATE"] != 0
states2 = allPop.loc [row_constraint, "NAME"]
print(states2)
print(states == states2)

#2e
print('Q2e:\n')
myPop = pd.DataFrame(allPop, columns = ['REGION', 'STATE', 'NAME', 'POPESTIMATE2010'])
myPop = myPop[5:]
print(myPop)
print(myPop.rename(columns = {'POPESTIMATE2010' : 'POPULATION'}))
myPop['REGION'][myPop['REGION'] == 'X'] = '5'    
myPop['REGION'] = pd.to_numeric(myPop['REGION'])
myPop.reset_index(drop = True, inplace = True)
print(myPop)
pop = pd.read_csv('pop.csv')




