#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 15:20:48 2020

@author: hajrashahab
"""

import pandas as pd
import numpy as np

#1
weather = pd.read_csv('weather5.csv')
print(weather)
print('Weather table columns: ', weather.columns)
print('No. of cols: ', len(weather.columns))
print('No. of rows: ', len(weather['Temperature'])) 

weather = weather.dropna()
weather = weather.reset_index(drop=True)
print('No. of rows(without NaN): ', len(weather['Temperature'])) 


def Filter(x): 
    if x  > 100:
        return 100
    elif x < 0:
        return 0
    else:
        return x

            
weather['Humidity'] = weather['Humidity'].apply(Filter) 
print(weather) 


#2 
def toTime(x):
    y = x.split(':')
    y_int = int(y[0])
    if y_int < 12: 
        return x + ' AM'
    elif y_int == 12:
        return x + ' PM'
    elif y_int >= 12:
        return str(y_int - 12) + ":" + y[1] + ' PM'


def toTime2(x):
    y = x.split(':')
    y_int = int(y[0])
    str_y_int = str(y_int)
    if y_int < 12: 
        if len(str_y_int) < 2:
            str_y_int = '0' + str_y_int
        return str_y_int + ":" + y[1] + ' AM'
    elif y_int == 12:
        return str(y_int) + ":" + y[1]+ ' PM'
    elif y_int >= 12:
        if len(str_y_int) < 2:
            str_y_int = '0' + str_y_int + ":" + y[1]
            return '0' + str(y_int - 12) + ":" + y[1] + ' PM'
        else:
            return str(y_int - 12) + ":" + y[1] + ' PM'

hour = list()
am_pm = list()
for n in range(weather['Time'].count()):
    hour.append(toTime2(weather['Time'].iloc[n])[:5]) 
    am_pm.append(toTime2(weather['Time'].iloc[n])[5:]) 
print(weather)
weather['12Hour'] = hour
weather['AM-PM'] = am_pm
print(weather)

# str_y_int = str(y_int)
# if len(str_y_int) < 2:
#     str_y_int = '0' + str_y_int
    
    
# look for number spaces and adjust for AM-PM 
weather.groupby(['AM-PM']).count()


print('Q2:\n')                                             
weather = weather[['Time', '12Hour', 'AM-PM', 'Temperature', 'Humidity', 'Wind', 'Clouds']]
print(weather)


#3 
print('Q3:\n')
def toMinutes(x): 
    x1 = x.split(":")
    for i in range(0, len(x1)):
        x1[i] = int(x1[i]) 
    print(x1)
    return x1[0] * 60 + x1[1]

weather['Elapsed'] = weather['Time'].apply(toMinutes) 
print(weather['Elapsed'])
weather = weather[['Time', '12Hour', 'AM-PM', 'Elapsed', 'Temperature', 'Humidity', 'Wind', 'Clouds']]
print(weather)

import matplotlib.pyplot as plt 

#4
print('Q4:\n')                                    
plt.title('Temperature Data')                                   
cols = weather.columns
plt.xlabel(cols[3]) 
plt.ylabel(cols[4]) 
plt.scatter(weather['Elapsed'], weather['Temperature'], marker='*', color='blue')
plt.show()


#5
plt.title('Humidity Data') 
cols = weather.columns
plt.xlabel(cols[3]) 
plt.ylabel(cols[5]) 
plt.plot(weather['Elapsed'], weather['Humidity'], marker='*', color='green')
plt.show()


#6
plt.xlabel('Wind') 
plt.hist(weather['Wind'], bins = 5)                     
plt.show()

#7
plt.title('Temperature Data')                           
cols = weather.columns
plt.xlabel(cols[3]) 
plt.ylabel(cols[4]) 
max_temp = max(weather['Temperature'])
plt.ylim(ymin = 0, ymax = max_temp + 1)
plt.scatter(weather['Elapsed'], weather['Temperature'], marker='*', color='blue') 
plt.show()

#8
import numpy as np
import random
import seaborn as sns 

x = str(round(weather['Temperature'].corr(weather['Humidity']), 2))
plt.title('Temperature x Humidity, Correlation = ' + x)
cols = weather.columns
sns.regplot(x = 'Temperature', y = 'Humidity', data = weather)

#9
sns.relplot(x='Elapsed', y='Temperature', col='AM-PM', size='Temperature', sizes =(20,200), 
            data=weather)


sns.relplot(x='Elapsed', y='Temperature', col='Clouds', size='Temperature', sizes =(20,200), 
            data=weather) 

#10
sns.factorplot(x='Clouds', y='Temperature', col = 'AM-PM', kind='bar', data= weather) #separate graph for AM-PM

sns.factorplot(x='Clouds', y='Temperature', col = 'AM-PM', kind='box', data= weather)  #separate graph for AM-PM








