import copy

from RandomAlgoWeb.RandomAlgo.ListHolder import Listholder
from RandomAlgoWeb.RandomAlgo.Utils import createUsersNonRandomFromDB, createDays, fillDaysWithUsersFromDB, \
    areAllDaysValid, createUsersNonRandom, fillDaysWithUsers
import math


# This method runs until it finds a valid schedule, based on the users it gets from the argument.
def runUntilCorrectWithUsers(users):
    numberOfDays = 5

    foundSolution = True
    firstFoundSolution = Listholder
    dayBuilds = [1, 0, 0, 0]

    count = 0

    while foundSolution:
        if count % 100 == 0:
            print(count)
        dbUsers = createUsersNonRandomFromDB(copy.deepcopy(users))
        # days = createDays(numberOfDays, dayBuilds, math.floor(len(users)) / 5)
        days = createDays(numberOfDays, dayBuilds, 1)

        newListHolderTry = fillDaysWithUsersFromDB(days, dbUsers)
        if areAllDaysValid(newListHolderTry):
            firstFoundSolution = newListHolderTry
            foundSolution = False
        count += 1

    print("It took " + str(count) + " tries")
    return firstFoundSolution


# This method runs the algorithm X amount of times, and then return all the valid results in a list.
def runXTimes(x):
    correctResults = []

    numberOfDays = 5

    dayBuilds = [1, 1, 1, 1]
    userBuilds = [2, 2, 2, 2]
    numberOfUsers = 8
    for i in range(x):
        nonRandomUsers = createUsersNonRandom(copy.deepcopy(userBuilds))
        days = createDays(numberOfDays, dayBuilds)

        newListHolderTry = fillDaysWithUsers(days, nonRandomUsers)
        if areAllDaysValid(newListHolderTry):
            correctResults.append(newListHolderTry)
        print(i)
    print("We have " + str(len(correctResults)) + " correct results")


def runUntilCorrect():
    numberOfDays = 5
    dayBuilds = [1, 1, 1, 1]
    userBuilds = [2, 2, 2, 2]
    numberOfUsers = 8

    foundSolution = True
    firstFoundSolution = Listholder
    count = 0
    while foundSolution:
        print(count)
        nonRandomUsers = createUsersNonRandom(copy.deepcopy(userBuilds))
        days = createDays(numberOfDays, dayBuilds)

        newListHolderTry = fillDaysWithUsers(days, nonRandomUsers)
        if areAllDaysValid(newListHolderTry):
            firstFoundSolution = newListHolderTry
            foundSolution = False
        count += 1

    print("It took " + str(count) + " tries")
    return firstFoundSolution
