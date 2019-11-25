startDay = 11

class Day:
    def __init__(self, dayNumber, numberOfUsersRequired):
        self.numberOfUsersRequired = numberOfUsersRequired
        self.dayNumber = dayNumber
        self.usersForTheDay = []
        self.date = startDay + dayNumber

    def isDayValid(self):
        valid = True
        for x in self.numberOfUsersRequired:
            if x != 0:
                valid = False
        return valid

    def doesDayNeedJob(self, jobEnum):
        if self.numberOfUsersRequired[jobEnum.value] > 0:
            return True
        else:
            return False

    def getDayNumber(self):
        return self.dayNumber

    def addUser(self, user):
        self.usersForTheDay.append(user)
        user.addDay(self)
        self.numberOfUsersRequired[user.job.value] = self.numberOfUsersRequired[user.job.value] - 1

    def usersForTheDayToString(self):
        string = ""
        for x in self.usersForTheDay:
            string = string + str(x.ID) + ", "
        string = string[:-2]

        return string
