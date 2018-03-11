# The staticmethod() built-in function returns a static method for a given function.

# Example 1: Create a static method using staticmethod()
class Mathematics:

    def addNumbers(x, y):
        return x + y

# create addNumbers static method
Mathematics.addNumbers = staticmethod(Mathematics.addNumbers)

print('The sum is:', Mathematics.addNumbers(5, 10))


# Example 2: Create utility function as a static method
class Dates:
    def __init__(self, date):
        self.date = date

    def getDate(self):
        return self.date

    @staticmethod
    def toDashDate(date):
        return date.replace("/", "-")

date = Dates("15-12-2016")
dateFromDB = "15/12/2016"
dateWithDash = Dates.toDashDate(dateFromDB)

if(date.getDate() == dateWithDash):
    print("Equal")
else:
    print("Unequal")

# Example 3: How inheritance works with static method?
class Dates:
    def __init__(self, date):
        self.date = date

    def getDate(self):
        return self.date

    @staticmethod
    def toDashDate(date):
        return date.replace("/", "-")

class DatesWithSlashes(Dates):
    def getDate(self):
        return Dates.toDashDate(self.date)

date = Dates("15-12-2016")
dateFromDB = DatesWithSlashes("15/12/2016")

if(date.getDate() == dateFromDB.getDate()):
    print("Equal")
else:
    print("Unequal")
