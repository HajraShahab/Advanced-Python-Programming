# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 04:06:40 2020

@author: hshahab, mmansur 
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def filter(value):
    if(value > 100):
        return(100)
    elif(value < 0):
        return(0)
    else:
        return(value)

def toTime(timeVal):
    twelveHourTime = list()
    am_pm = ""
    hoursMins = timeVal.split(":")
    hour = int(hoursMins[0])
    mins = int(hoursMins[1])
    if(hour == 12):
        if(mins == 0):
            twelveHourTime.append("12")
            twelveHourTime.append("00")
        elif(mins < 10):
            twelveHourTime.append("12")
            twelveHourTime.append("0" + str(mins))
        else:
            twelveHourTime.append("12")
            twelveHourTime.append(str(mins))
        am_pm = "PM"
    elif(hour < 12):
        if(mins == 0):
            twelveHourTime.append(str(hour))
            twelveHourTime.append("00")
        elif(mins < 10):
            twelveHourTime.append(str(hour))
            twelveHourTime.append("0" + str(mins))
        else:
            twelveHourTime.append(str(hour))
            twelveHourTime.append(str(mins))
        am_pm = "AM"
    elif(hour > 12):
        if(mins == 0):
            twelveHourTime.append(str(hour - 12))
            twelveHourTime.append("00")
        elif(mins < 10):
            twelveHourTime.append(str(hour - 12))
            twelveHourTime.append("0" + str(mins))
        else:
            twelveHourTime.append(str(hour - 12))
            twelveHourTime.append(str(mins))
        am_pm = "PM"
    strTime = (twelveHourTime[0] + ":" + twelveHourTime[1])
    return(strTime, am_pm)

def toMinutes(timeVal):
    hoursMins = timeVal.split(":")
    hour = int(hoursMins[0])
    mins = int(hoursMins[1])
    totalMins = hour*60 + mins
    return(int(totalMins))

# 1
weather = pd.read_csv("weather5.csv")
print("weather: ")
print(weather)
print("\n")

print("Weather table columns: %s" % (', ').join(list(weather.columns)))

print("Number of columns of weather: %d" % (len(weather.iloc[0])))

print("Number of rows of weather: %d" % (len(list(weather["Temperature"]))))

weather.dropna(inplace=True)
print("Number of rows of weather after removing NA: %d" % (len(list(weather["Temperature"]))))
print("\n")

weather["Humidity"] = weather["Humidity"].apply(filter)
print('\nweather after removing bad humidity values: ')
print(weather)
print('\n')


# 2
weatherTime = list()
weatherMins = list()
for i in weather.index:
    weatherTime.append(weather["Time"].apply(toTime)[i][0])
    weatherMins.append(weather["Time"].apply(toTime)[i][1])
weather["12Hour"] = weatherTime
weather["AM-PM"] = weatherMins

print("\nFormatted table for 2: \n")

print("%5s  %7s  %6s  %12s  %9s  %5s  %14s" % ("Time", "12Hour", "AM-PM",
                                               "Temperature", "Humidity",
                                               "Wind", "Clouds"))
for i in weather.index:
    print("%5s  %7s  %6s  %12.1f  %9.1f  %5.1f  %14s" % (weather.loc[i]["Time"],
                                                         weather.loc[i]["12Hour"],
                                                         weather.loc[i]["AM-PM"],
                                                         weather.loc[i]["Temperature"],
                                                         weather.loc[i]["Humidity"],
                                                         weather.loc[i]["Wind"],
                                                         weather.loc[i]["Clouds"]))


# 3

weather["Elapsed"] = weather["Time"].apply(toMinutes)

print("\nFormatted table for 3: \n")
print("%5s  %7s  %6s  %8s  %12s  %9s  %5s  %14s" % ("Time", "12Hour", "AM-PM",
                                                   "Elapsed", "Temperature",
                                                   "Humidity", "Wind", "Clouds"))
for i in weather.index:
    print("%5s  %7s  %6s  %8d  %12.1f  %9.1f  %5.1f  %14s" % (weather.loc[i]["Time"],
                                                         weather.loc[i]["12Hour"],
                                                         weather.loc[i]["AM-PM"],
                                                         weather.loc[i]["Elapsed"],
                                                         weather.loc[i]["Temperature"],
                                                         weather.loc[i]["Humidity"],
                                                         weather.loc[i]["Wind"],
                                                         weather.loc[i]["Clouds"]))
    
# 4

plt.title("Temperature Data")
plt.xlabel("Elapsed")
plt.ylabel("Temperature")
plt.scatter(weather["Elapsed"], weather["Temperature"])
plt.figure(1)
plt.show()


# 5

plt.title("Humidity Data")
plt.xlabel("Elapsed")
plt.ylabel("Humidity")
plt.plot(weather["Elapsed"], weather["Humidity"])
plt.figure(2)
plt.show()

# 6

plt.title("Wind")
plt.hist(weather["Wind"], bins = 5)
plt.figure(3)
plt.show()

# 7

# plt.title("Temperature Data")
# plt.xlabel("Elapsed")
# plt.ylabel("Temperature")
# plt.ylim(0,1)
# plt.scatter(weather["Elapsed"], weather["Temperature"])
# plt.figure(4)
# plt.show()

plt.title('Temperature Data')                           
cols = weather.columns
plt.xlabel(cols[3]) 
plt.ylabel(cols[4]) 
max_temp = max(weather['Temperature'])
plt.ylim(ymin = 0, ymax = max_temp + 1)
plt.scatter(weather['Elapsed'], weather['Temperature'], marker='*', color='blue') 
plt.figure(4)
plt.show()


# 8

weatherCorr = weather.corr()
x = weatherCorr.loc["Temperature"]["Humidity"]
# print(x)
plt.title("Temperature x Humidity, Correlation = %.3f" % (x))
sns.regplot(data = weather, x = "Temperature", y = "Humidity")
plt.figure(5)
plt.show()

# 9

sns.relplot(x = "Elapsed", y = "Temperature", col = "AM-PM",  
            size='Temperature', sizes=(20,200), data = weather)
plt.figure(6)
plt.show()

sns.relplot(x = "Elapsed", y = "Temperature", col = "Clouds",  
            size='Temperature', sizes=(20,200), data = weather)
plt.figure(7)
plt.show()

# 10

sns.factorplot(x = "Clouds", y = "Temperature", 
                kind = "bar", col = "AM-PM", data = weather)
plt.figure(8)
plt.show()

sns.factorplot(x = "Clouds", y = "Temperature", 
                kind = "box", col = "AM-PM", data = weather)
plt.figure(9)
plt.show()













