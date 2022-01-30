#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 09:35:27 2020

@author: hajrashahab
"""

import sqlite3
import pandas as pd

#1
print('Q1:\n')
with open('JustLeeBooks.txt') as fin:
    print(fin)
    commands = []
    for i in fin:
        if len(i) > 0: 
            commands.append(i)
            commands = [i.upper() for i in commands] 
    print(commands)
    
#2
print('Q2:\n')
try:
    connection = sqlite3.connect('LeeBooks.db.sqlite3') 
    cursor = connection.cursor()
    for command in commands:
        cursor.execute(command)
        connection.commit()
except Exception as e:
    print(e)

#3
print('Q3:\n')  
query = """
SELECT name FROM sqlite_master WHERE type = 'table';"""
cursor.execute(query)
tb_rows = cursor.fetchall()

for row in tb_rows:
    print("\nTable: ", row[0])
    query = 'PRAGMA table_info(' + row[0] + ')'
    cursor.execute(query)
    col_rows = cursor.fetchall()
    print('Columns: ', end = " | ") 
    for i in col_rows:
        print(i[1], end = " | ") 
    print()
#4 
print('\nQ4:')
query ="""
SELECT LASTNAME, FIRSTNAME, STATE
FROM CUSTOMERS;"""
cursor.execute(query)
rows = cursor.fetchall()
for row in rows:
    print(row)
customersDF = pd.DataFrame(rows, columns = ['LASTNAME', 'FIRSTNAME', 'STATE']) 
print(customersDF)
customersDF.sort_values(by = 'STATE', inplace = True)
print(customersDF)
customersDF.sort_values(by = ['STATE', 'LASTNAME'], inplace = True) 
print(customersDF)


#5
print('\nQ5:')
query ="""
SELECT ORDERNUM, QUANTITY, PAIDEACH
FROM ORDERITEMS;""" 
cursor.execute(query)
rows = cursor.fetchall()
for row in rows:
    print(row)
orderItemsDF = pd.DataFrame(rows, columns = ['ORDERNUM', 'QUANTITY', 'PAIDEACH']) 
print(orderItemsDF)
orderItemsDF['TOTAL'] = orderItemsDF['QUANTITY'] * orderItemsDF['PAIDEACH'] 
print(orderItemsDF)
print('Overall TOTAL: $', orderItemsDF['TOTAL'].sum()) 

#6
print('Q6:\n') 
query = """
CREATE TABLE BOOKLIST AS 
SELECT LNAME, FNAME, TITLE
from BOOKS, AUTHOR, BOOKAUTHOR
WHERE BOOKS.ISBN = BOOKAUTHOR.ISBN AND BOOKAUTHOR.AuthorID = Author.AuthorID;""" 

cursor.execute(query)
query = "SELECT * FROM BOOKLIST"
cursor.execute(query)
rows = cursor.fetchall()
for row in rows: 
    print(row)
type(row) 

#7
print('Q7:\n')  
bookListDF = pd.DataFrame(rows, columns = ['LNAME', 'FNAME', 'TITLE']) 
print(bookListDF)
bookListDF.sort_values(by = ['LNAME', 'FNAME'], inplace = True) 
print(bookListDF)
bookListDF = bookListDF.groupby(by = ['LNAME']).count()
print(bookListDF)

#Two or more people can have the same last name. For instance, there are two different authors who share the 
#same last name, i.e. WHITE. The count function counts them as one author instead of two thus attributing 4 books 
#to the same author instead of two different authors.  

#8
print('Q8:\n')  
query = """
SELECT name FROM sqlite_master WHERE type = 'table';"""
cursor.execute(query)
tb_rows = cursor.fetchall()

for row in tb_rows:
    print("\nTable: ", row[0])
    query = 'PRAGMA table_info(' + row[0] + ')'
    cursor.execute(query)
    col_rows = cursor.fetchall()
    print('Columns: ', end = " | ") 
    for i in col_rows:
        print(i[1], end = " | ") 
    query = """SELECT COUNT (*) FROM %s""" % row[0] 
    cursor.execute(query) 
    t1_rows = cursor.fetchone()[0] 
    print('\n#', 'Rows = ', t1_rows)
    

    












