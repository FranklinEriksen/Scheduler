from RandomAlgoWeb.RandomAlgo.UserEnum import *
from RandomAlgoWeb.RandomAlgo.User import *
from RandomAlgoWeb.RandomAlgo.Day import *
from RandomAlgoWeb.RandomAlgo.ListHolder import Listholder
import random
import copy


def areAllDaysValid(listholder):
    result = True

    for day in listholder.days:
        if not day.isDayValid():
            result = False

    for user in listholder.users:
        if user.getLongestChainOfWorkDaysNumber() > 4:
            result = False
    return result


def fillDaysWithUsers(days, users):

    for day in days:
        tempUsers = []
        for x in users:
            tempUsers.append(x)
        usersRemaining = True
        while usersRemaining:
            tempUsersAmount = len(tempUsers)
            tempUser = random.choice(tempUsers)

            if day.doesDayNeedJob(tempUser.job) and tempUser.canUserWorkDay(day):
                day.addUser(tempUser)
            tempUsers.remove(tempUser)

            # print(day.numberOfUsersRequired)
            if day.isDayValid():
                usersRemaining = False
            elif len(tempUsers) <= 0:
                usersRemaining = False


    listHolder = Listholder(days, users)

    return listHolder


def fillDaysWithUsersFromDB(days, users):

    for day in days:
        tempUsers = []
        for x in users:
            if list(x.avaibleDays)[day.dayNumber] == "1":
                tempUsers.append(x)
        usersRemaining = True
        while usersRemaining:
            tempUsersAmount = len(tempUsers)
            tempUser = random.choice(tempUsers)

            if day.doesDayNeedJob(tempUser.job) and tempUser.canUserWorkDay(day):
                day.addUser(tempUser)
            tempUsers.remove(tempUser)

            # print(day.numberOfUsersRequired)
            if day.isDayValid():
                usersRemaining = False
            elif len(tempUsers) <= 0:
                usersRemaining = False


    listHolder = Listholder(days, users)

    return listHolder


def createDays(numberOfDays, dayBuilds):
    days = []
    for i in range(numberOfDays):
        days.append(Day(i, copy.deepcopy(dayBuilds)))
    return days


def createUsersNonRandom(userBuild):
    users = []
    id = 0
    for i in range(len(userBuild)):
        for j in range(userBuild[i]):
            users.append(User(UserEnum(i), id))
            id = id + 1
    return users


def createUsersNonRandomFromDB(usersFromDB):
    users = []
    id = 0
    for j in usersFromDB:
        users.append(User(UserEnum(0), id, j.days, j.Name))
        id = id + 1
    for user in users:
        print("name = " + str(user.name))
    return users


def createUsersRandom(numberOfUsers):
    users = []
    for i in range(numberOfUsers):
        users.append(User(random.choice(list(UserEnum)), i))
    return users
