from RandomAlgoWeb.RandomAlgo.Day import *
from RandomAlgoWeb.RandomAlgo.User import *


#   The final object with the complete schedule and all of the users to be passed around.
class Listholder:
    def __init__(self, days, users):
        self.days = days
        self.users = users
