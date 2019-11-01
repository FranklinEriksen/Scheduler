from enum import Enum
class UserEnum(Enum):
    Job1 = 0
    Job2 = 1
    Job3 = 2
    Job4 = 3

    def toString(self):
        return self.value
