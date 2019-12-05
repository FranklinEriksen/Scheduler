#test cases for RandomAlgo
import unittest
from RandomAlgoWeb.RandomAlgo.Day import *
from RandomAlgoWeb.RandomAlgo.User import *

class UserTest(unittest.TestCase):
    def test_init(self):
        u = User('worker', 123)
        v = User('worker', 124, [0, 1, 2], 'Hank')

    def testCanUserWorkDay(self):
        u = User('Worker', 125, [0, 1, 2])
        self.assertTrue(u.canUserWorkDay(2))
        self.assertFalse(u.canUserWorkDay(3))

    def testGetLongestChainOfWorkDays(self):
        days = [
            Day(0, 2),
            Day(1, 2),
            Day(2, 2),
            Day(3, 2)
        ]
        u = User('Worker', 126, [0, 1, 3])
        v = User('Worker', 127, [0, 2, 3])
        for i in [0, 1, 3]:
            u.addDay(days[i])
        for i in [0, 2, 3]:
            v.addDay(days[i])
        self.assertEqual(2, u.getLongestChainOfWorkDaysNumber())
        self.assertEqual(2, v.getLongestChainOfWorkDaysNumber())


class DayTest(unittest.TestCase):
    def test_init(self):
        Day(0, 0)
        Day(4, 6)
        Day(-1, 0) # should fail
        Day(0, -1) # should also fail

if __name__ == '__main__':
    unittest.main()