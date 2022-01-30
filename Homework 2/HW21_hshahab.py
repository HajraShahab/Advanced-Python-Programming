#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 09:14:40 2020

@author: hajrashahab
"""

#Problem1 

import pandas as pd

def menu():
     print('1. Display the entire table')
     print('2. Display the total population of all the states')
     print('3. Prompt for the name of a state. Display its population')
     print('4. Display the table sorted by state name')
     print('5. Display the table grouped by region')
     print('6. Display the table sorted by population, largest to smallest')
     print('0. Quit')
     choice = int(input('Enter your choice: '))
     return choice


def main():
    pop = pd.read_csv('pop.csv')
    print(pop)
    while True:
        menu_choice = menu()
        if menu_choice == 1:
            print(pop)
        elif menu_choice == 2:
            print('Total Population: ', pop['POPULATION'].sum())
        elif menu_choice == 3:
            state = input ('Enter the name of a state to find corresponding population: ')
            if state in pop.values:
                row_constraint = pop['NAME'] == state
                print('Population of state entered: ', state, pop.loc[row_constraint, 'POPULATION'].to_string (index = False))
            else:
                print('State not found')
        elif menu_choice == 4:
            print(pop.sort_values(by ='NAME'))
        elif menu_choice == 5: 
            print(pop.sort_values(by ='REGION'))
        elif menu_choice == 6:
            print(pop.sort_values(by='POPULATION', ascending = False))
        elif menu_choice == 0:
            print('Successfully quit')
            break
        else:
            print('Error, please try again') 
            

if __name__ == '__main__': 
    main()