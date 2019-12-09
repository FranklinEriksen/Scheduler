
# The user object. Consists of all of the information used by each individual user. Also contains a list of all days each user is going to work.
class User:
    def __init__(self, job, ID, availableDays, name=None, availableHours=None):
        self.job = job
        self.ID = ID
        self.workDays = []
        self.longestChainOfWorkDaysNumber = 0
        self.availableDays = availableDays
        self.name = name
        self.availableHours = availableHours
        self.eachDayInHours = []


#   Check to see if the current worker can work the selected day
    def canUserWorkDay(self, testDay):
        if len(self.workDays) != 0:
            for day in self.workDays:
                if day.getDayNumber() == testDay.getDayNumber():
                    return False
        test = list(self.availableDays)
        if str(test[testDay.getDayNumber()]) == "1":
            return True
        return False


#   Check to see if the user can work in the specified hours
    def canUserWorkHourSlotOnDay(self, dayNumber, startHour, endHour):
        theDay = self.availableHours[dayNumber]
        for x in range(startHour, endHour):
            if theDay[x] != "1":
                return False
        return True


#   Add the day to the users days
    def addDay(self, day):
        self.workDays.append(day)


#   What is the longest chain of working days. Is used to make sure no user is working more than a set amount of days in row.
    def getLongestChainOfWorkDaysNumber(self):
        maxCounter = 0
        counter = 0
        for i in range(len(self.workDays) - 1):
            if self.workDays[i].getDayNumber() == (self.workDays[i + 1].getDayNumber() - 1):
                counter = counter + 1
                if counter > maxCounter:
                    maxCounter = counter
            else:
                counter = 0
        self.longestChainOfWorkDaysNumber = maxCounter
        return self.longestChainOfWorkDaysNumber


#   Tells the user which days they are gonna work.
    def setEachDayWorkHours(self, dayNumber, startHourIndex, endHourIndex):
        self.eachDayInHours.append([dayNumber, startHourIndex, endHourIndex])

