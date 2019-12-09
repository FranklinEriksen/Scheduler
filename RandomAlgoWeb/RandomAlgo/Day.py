startDay = 9


#The day object. Consists of all of the information used by each individual day.
class Day:
    def __init__(self, dayNumber, numberOfUsersRequired, usersPerHour=0):
        self.numberOfUsersRequired = numberOfUsersRequired
        self.dayNumber = dayNumber
        self.usersForTheDay = []
        self.dayInHours = [usersPerHour] * 24
        self.date = startDay + dayNumber

#   Checks if the current day setup is viable.
    def isDayValid(self):
        for x in self.numberOfUsersRequired:
            if x != 0:
                return False
        for x in self.dayInHours:
            if x != 0:
                return False
        return True

#   Does this day need another user with that specific job
    def doesDayNeedJob(self, jobEnum):
        if self.numberOfUsersRequired[jobEnum.value] > 0:
            return True
        else:
            return False

#   Does the day need another user with these hours?
    def doesDayNeedUsersHours(self, user):
        usersDay = user.availableHours[self.dayNumber]
        maxCount = 0
        count = 0
        startIndex = 0
        endIndex = 0
        requirement = 4
        for x in range(0, 24):
            if usersDay[x] == "1" and self.dayInHours[x] >= 1:
                count += 1
            else:
                if count > 0 and count > maxCount:
                    maxCount = count
                    count = 0
                    endIndex = x
                    startIndex = x-maxCount
        if maxCount == 0:
            endIndex = 24
            startIndex = endIndex - count
            maxCount = count
        if maxCount >= requirement:
            return True, startIndex, endIndex
        return False, startIndex, endIndex

    def getDayNumber(self):
        return self.dayNumber

#   Adds the user to the day as a worker, and updates the user aswell.
    def addUser(self, user, startHourIndex, endHourIndex, day):
        self.usersForTheDay.append(user)
        user.addDay(self)
        self.numberOfUsersRequired[user.job.value] = self.numberOfUsersRequired[user.job.value] - 1
        for x in range(startHourIndex, endHourIndex):
            day.dayInHours[x] -= 1
        user.setEachDayWorkHours(day.dayNumber, startHourIndex, endHourIndex)

#   Return all who works this day
    def usersForTheDayToString(self):
        string = ""
        for x in self.usersForTheDay:
            string = string + str(x.ID) + ", "
        string = string[:-2]

        return string
