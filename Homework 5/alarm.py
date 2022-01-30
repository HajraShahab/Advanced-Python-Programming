# TBD
# Needs:
# - constructor with location parameter; hard-codes message
# - getLocation, returns the location
# - soundAlarm, simulates the alarm going off by printing the messaga and location
# - __str__, returns the message and location as one string
class Alarm:
    def __init__(self, location):
        self._location = location
        self._message = "Warning! Warning!"
        
    def getLocation(self):
        return(self.location)

    def soundAlarm(self):
        print(self._message + ", " + self._location)
        
    def __str__(self):
        return("Alarm sounding for location: " + self._location + " " + self._message)
        
    