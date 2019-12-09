import copy

from RandomAlgoWeb.RandomAlgo.ListHolder import Listholder
from RandomAlgoWeb.RandomAlgo.Utils import createUsersNonRandomFromDB, createDays, fillDaysWithUsersFromDB, \
    areAllDaysValid, createUsersNonRandom, fillDaysWithUsers
import math

numberOfDays = 7

# This method runs until it finds a valid schedule, based on the users it gets from the argument.
def runUntilCorrectWithUsers(users):

    foundSolution = True
    firstFoundSolution = Listholder
    dayBuilds = [3, 0, 0, 0]

    count = 0

    while foundSolution:
        if count % 100 == 0:
            print(count)
        dbUsers = createUsersNonRandomFromDB(copy.deepcopy(users))
        days = createDays(numberOfDays, dayBuilds, 1)

        newListHolderTry = fillDaysWithUsersFromDB(days, dbUsers)
        if areAllDaysValid(newListHolderTry):
            firstFoundSolution = newListHolderTry
            foundSolution = False
        count += 1

    return firstFoundSolution


# This method runs the algorithm X amount of times, and then return all the valid results in a list.
def runXTimes(x):
    correctResults = []

    numberOfDays = 5

    dayBuilds = [1, 1, 1, 1]
    userBuilds = [2, 2, 2, 2]
    for i in range(x):
        nonRandomUsers = createUsersNonRandom(copy.deepcopy(userBuilds))
        days = createDays(numberOfDays, dayBuilds)

        newListHolderTry = fillDaysWithUsers(days, nonRandomUsers)
        if areAllDaysValid(newListHolderTry):
            correctResults.append(newListHolderTry)
    print("We have " + str(len(correctResults)) + " correct results")


def runUntilCorrect():
    numberOfDays = 5
    dayBuilds = [1, 1, 1, 1]
    userBuilds = [2, 2, 2, 2]

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
