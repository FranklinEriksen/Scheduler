from RandomAlgoWeb.RandomAlgo.JobEnum import *
from RandomAlgoWeb.RandomAlgo.User import *
from RandomAlgoWeb.RandomAlgo.Day import *
from RandomAlgoWeb.RandomAlgo.ListHolder import Listholder
import random
import copy


# Check if the schedule is valid. First if all days are valid, then if all users doesn't work too many days in row.
def areAllDaysValid(listHolder):

    for day in listHolder.days:
        if not day.isDayValid():
            return False

    for user in listHolder.users:
        if user.getLongestChainOfWorkDaysNumber() > 4:
            return False
    return True


# Takes the days argument and randomly fills it with the given users.
def fillDaysWithUsers(days, users):
    for day in days:
        tempUsers = []
        for x in users:
            tempUsers.append(x)
        usersRemaining = True
        while usersRemaining:
            tempUser = random.choice(tempUsers)

            if day.doesDayNeedJob(tempUser.job) and tempUser.canUserWorkDay(day):
                day.addUser(tempUser)
            tempUsers.remove(tempUser)

            if day.isDayValid():
                usersRemaining = False
            elif len(tempUsers) <= 0:
                usersRemaining = False

    listHolder = Listholder(days, users)

    return listHolder


# Takes the days argument and randomly fills it with the given users. This one takes from the DB, and checks if they
# are available for the specific day
def fillDaysWithUsersFromDB(days, users):

    for day in days:
        tempUsers = []
        for x in users:
            if list(x.availableDays)[day.dayNumber] == "1":
                tempUsers.append(x)
        usersRemaining = True
        while usersRemaining:
            tempUser = random.choice(tempUsers)
            dayNeedsOfUser = day.doesDayNeedUsersHours(tempUser)
            if day.doesDayNeedJob(tempUser.job) and tempUser.canUserWorkDay(day) and dayNeedsOfUser[0]:
                day.addUser(tempUser, dayNeedsOfUser[1], dayNeedsOfUser[2], day)
            tempUsers.remove(tempUser)

            if day.isDayValid():
                usersRemaining = False
            elif len(tempUsers) <= 0:
                usersRemaining = False

    listHolder = Listholder(days, users)
    return listHolder


# Creates a list of days, each with copy of how many employees it needs for the day.
def createDays(numberOfDays, dayBuilds, usersPerHour):
    days = []
    for i in range(numberOfDays):
        days.append(Day(i, copy.deepcopy(dayBuilds), usersPerHour))
    return days


# Given a userBuild, would generate a list of users. A userBuild would look like : [2,1,1,4]. Each index corresponds
# to a Job value from the JobEnum.
def createUsersNonRandom(userBuild):
    users = []
    id = 0
    for i in range(len(userBuild)):
        for j in range(userBuild[i]):
            users.append(User(JobEnum(i), id))
            id = id + 1
    return users


def createUsersNonRandomFromDB(usersFromDB):
    users = []
    id = 0
    for j in usersFromDB:
        availableHours = [j.mon, j.tues, j.wed, j.thurs, j.fri, j.sat, j.sun]
        users.append(User(JobEnum(0), id, j.days, j.Name, availableHours))
        id = id + 1

    return users


def createUsersRandom(numberOfUsers):
    users = []
    for i in range(numberOfUsers):
        users.append(User(random.choice(list(JobEnum)), i))
    return users
