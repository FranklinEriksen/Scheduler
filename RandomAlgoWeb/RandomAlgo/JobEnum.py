from enum import Enum

# This is an enum to be put into each user. If we look at Walmart as a workplace, each job could be stocker, cashier,
# cleaner and so on.
class JobEnum(Enum):
    Job1 = 0
    Job2 = 1
    Job3 = 2
    Job4 = 3

    def toString(self):
        return self.value
