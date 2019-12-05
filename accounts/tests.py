from django.test import TestCase
from accounts import views
# Create your tests here.

class AccountTests(TestCase):

    def getHoursTest(self):
        #These are all standard test cases
        self.assertEqual( views.getHours("01","10"), "011111111110000000000000")
        self.assertEqual( views.getHours("02","10"), "001111111110000000000000")
        self.assertEqual( views.getHours("02","11"), "001111111111000000000000")
        self.assertEqual( views.getHours("00","11"), "111111111111000000000000")
        self.assertEqual( views.getHours("00","12"), "111111111111100000000000")
        self.assertEqual( views.getHours("00","12"), "111111111111100000000000")
        self.assertEqual( views.getHours("00","13"), "111111111111110000000000")
        self.assertEqual( views.getHours("00","14"), "111111111111111000000000")
        self.assertEqual( views.getHours("00","15"), "111111111111111100000000")
        self.assertEqual( views.getHours("01","15"), "011111111111111100000000")
        self.assertEqual( views.getHours("03","15"), "000111111111111100000000")

        #these cover the corner cases for the algorithm
    def cornerCaseTest(self):
        self.assertEqual( views.getHours("00","10"), "111111111110000000000000")
        self.assertEqual( views.getHours("00","10"), "111111111110000000000000")
        self.assertEqual( views.getHours("00","11"), "111111111111000000000000")
        self.assertEqual( views.getHours("00","11"), "111111111111000000000000")
        self.assertEqual( views.getHours("00","12"), "111111111111100000000000")
        self.assertEqual( views.getHours("00","12"), "111111111111100000000000")
        self.assertEqual( views.getHours("00","13"), "111111111111110000000000")
        self.assertEqual( views.getHours("00","14"), "111111111111111000000000")
        self.assertEqual( views.getHours("00","15"), "111111111111111100000000")
        self.assertEqual( views.getHours("00","15"), "111111111111111100000000")
        self.assertEqual( views.getHours("00","15"), "111111111111111100000000")

        #Below are more corner cases close to 24 hours
        self.assertEqual( views.getHours("01","24"), "011111111111111111111111")
        self.assertEqual( views.getHours("02","24"), "001111111111111111111111")
        self.assertEqual( views.getHours("03","24"), "000111111111111111111111")
        self.assertEqual( views.getHours("04","24"), "000011111111111111111111")
        self.assertEqual( views.getHours("05","24"), "000001111111111111111111")
        self.assertEqual( views.getHours("06","24"), "000000111111111111111111")
        self.assertEqual( views.getHours("07","24"), "000000011111111111111111")
        self.assertEqual( views.getHours("08","24"), "000000001111111111111111")

        #What happens if the end time is before the start time?
        self.assertEqual( views.getHours("05","02"), "000000000000000000000000")
        self.assertEqual( views.getHours("12","06"), "000000000000000000000000")
        self.assertEqual( views.getHours("18","02"), "000000000000000000000000")
        self.assertEqual( views.getHours("24","04"), "000000000000000000000000")
        self.assertEqual( views.getHours("24","05"), "000000000000000000000000")
        self.assertEqual( views.getHours("5","2"), "000000000000000000000000")
        self.assertEqual( views.getHours("9","2"), "000000000000000000000000")
        self.assertEqual( views.getHours("9","3"), "000000000000000000000000")

        #Inputting nonsense
        self.assertEqual( views.getHours("~","_"), "000000000000000000000000")
        self.assertEqual( views.getHours("test","error"), "000000000000000000000000")
        self.assertEqual( views.getHours("~~~","err"), "000000000000000000000000")
        self.assertEqual( views.getHours("SDD","tests"), "000000000000000000000000")
        self.assertEqual( views.getHours("SDDS","test"), "000000000000000000000000")
        self.assertEqual( views.getHours("   ","  ok   "), "000000000000000000000000")



    def runAll(self):
        self.getHoursTest()
        self.cornerCaseTest()
