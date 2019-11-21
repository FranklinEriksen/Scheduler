class User:
    def __init__(self, job, ID, availableDays=None, name=None, availableHours=None):
        self.job = job
        self.ID = ID
        self.workDays = []
        self.longestChainOfWorkDaysNumber = 0
        self.availableDays = availableDays
        self.name = name
        self.availableHours = availableHours

    def canUserWorkDay(self, testDay):
        if len(self.workDays) != 0:
            for day in self.workDays:
                if day.getDayNumber() == testDay.getDayNumber():
                    return False
        return True

    def canUserWorkHourSlotOnDay(self, dayNumber, startHour, endHour):
        theDay = self.availableHours[dayNumber]
        for x in range(startHour, endHour):
            if theDay[x] != "1":
                return False
        return True


    def addDay(self, day):
        self.workDays.append(day)

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
