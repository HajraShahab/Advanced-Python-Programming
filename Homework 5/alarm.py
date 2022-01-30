# TBD
# Needs:
# - constructor with location parameter; hard-codes message
# - getLocation, returns the location
# - soundAlarm, simulates the alarm going off by printing the messaga and location
# - __str__, returns the message and location as one string
class Alarm:
    def __init__(self, location):
        self.__location = location
        self.__message = 'Warning! Warning!' 
    def getLocation(self, location):
        return self.__location
    def soundAlarm(self):
        print(self.__str__())
    def __str__(self):
        return self.__message  + ',' + self.__location 



