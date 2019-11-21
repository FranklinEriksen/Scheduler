class Day:
    def __init__(self, dayNumber, numberOfUsersRequired, usersPerHour=0):
        self.numberOfUsersRequired = numberOfUsersRequired
        self.dayNumber = dayNumber
        self.usersForTheDay = []
        self.date = 11 + dayNumber
        self.dayInHours = [usersPerHour] * 16

    def isDayValid(self):
        valid = True
        for x in self.numberOfUsersRequired:
            if x != 0:
                valid = False
        for x in self.dayInHours:
            if x != 0:
                valid = False
        return valid

    def doesDayNeedJob(self, jobEnum):
        if self.numberOfUsersRequired[jobEnum.value] > 0:
            return True
        else:
            return False

    def doesDayNeedUsersHours(self, user):
        usersDay = user.availableHours[self.dayNumber]
        maxCount, count, startIndex, endIndex  = 0
        requirement = 4
        for x in range(0, 16):
            if usersDay[x] == "1" and self.dayInHours >= 1:
                count += 1
            else:
                if count > 0 and count > maxCount:
                    maxCount = count
                    count = 0
                    endIndex = x
                    startIndex = x-maxCount
        if maxCount >= requirement:
            return True, startIndex, endIndex
        return False, startIndex, endIndex




    def getDayNumber(self):
        return self.dayNumber

    def addUser(self, user, startHourIndex, endHourIndex):
        self.usersForTheDay.append(user)
        user.addDay(self)
        self.numberOfUsersRequired[user.job.value] = self.numberOfUsersRequired[user.job.value] - 1
        for x in range(startHourIndex, endHourIndex):
            self.dayInHours[x] -= 1


    def usersForTheDayToString(self):
        string = ""
        for x in self.usersForTheDay:
            string = string + str(x.ID) + ", "
        string = string[:-2]

        return string
