#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 15:41:33 2020

@author: hajrashahab
"""

import json
import requests
import pandas as pd 


topic = ['Python', 'Data Science', 'Data Analysis', 'Machine Learning', 'Deep Learning'] #Part 1 
def fetchBook(topic): #Part 2
    headers = {'Content-Type': 'application/json'}
    url ='https://www.googleapis.com/books/v1/volumes?q=topic:' + topic
    response = requests.get(url, headers = headers)
    if response.status_code == 200:
        data = json.loads(response.content.decode('utf-8'))
        items = pd.io.json.json_normalize(data['items'])[['volumeInfo.title', 'volumeInfo.authors']] #Part 3 
        items = items.rename(columns = {'volumeInfo.title' : 'Title', 'volumeInfo.authors' : 'Authors'}) #Part 4
    return items[['Title', 'Authors']]
        
#Part 5
df1 = fetchBook(topic[0])
df2 = fetchBook(topic[1])
df3 = fetchBook(topic[2])
df4 = fetchBook(topic[3])
df5 = fetchBook(topic[4])


bigTable = pd.concat([df1, df2, df3, df4, df5], ignore_index = True)
print(bigTable)

#Part 6 
print('{:30}{:10}'.format('Title', 'Author')) 
for i in bigTable.index:
    if type(bigTable['Authors'].iloc[i]) is float:
        print('{:30}{:10}'.format(bigTable['Title'].iloc[i][:25], 'NA'))
    else:
        print('{:30}{:10}'.format(bigTable['Title'].iloc[i][:25], bigTable['Authors'].iloc[i][0]))