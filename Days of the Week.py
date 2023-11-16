"""
Your task is to implement a class called Weeker. Yes, your eyes don't 
deceive you – this name comes from the fact that objects of that class 
will be able to store and to manipulate the days of the week.

The class constructor accepts one argument – a string. The string 
represents the name of the day of the week and the only acceptable 
values must come from the following set:

Mon Tue Wed Thu Fri Sat Sun

Invoking the constructor with an argument from outside this set should 
raise the WeekDayError exception (define it yourself; don't worry, we'll
talk about the objective nature of exceptions soon). The class should 
provide the following facilities:

  - objects of the class should be "printable", i.e. they should be able 
	to implicitly convert themselves into strings of the same form as 
	the constructor arguments;
  - the class should be equipped with one-parameter methods called 
	add_days(n) and subtract_days(n), with n being an integer number and
	updating the day of week stored inside the object in the way 
	reflecting the change of date by the indicated number of days, 
	forward or backward.
  - all object's properties should be private;

Expected output

Mon
Tue
Sun
Sorry, I can't serve your request.
"""

class WeekDayError(Exception):
    pass
	

class Weeker:
    __days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    #Time complextiy: O(1)
    #Space complexity: O(1)
    def __init__(self, day):
        if day not in Weeker.__days:
            raise WeekDayError
        self.__dayNum = Weeker.__days.index(day)

    #Time complextiy: O(1)
    #Space complexity: O(1)
    def __str__(self):
        return Weeker.__days[self.__dayNum]

    #Time complextiy: O(1)
    #Space complexity: O(1)
    def add_days(self, n):
        self.__dayNum += n % 7
        if self.__dayNum >= 7:
            self.__dayNum -= 7
        
    #Time complextiy: O(1)
    #Space complexity: O(1)
    def subtract_days(self, n):
        self.__dayNum -= n % 7
        if self.__dayNum < 0:
            self.__dayNum += 7


if __name__ == "__main__":
    try:
        weekday = Weeker('Mon')
        print(weekday)
        weekday.add_days(15)
        print(weekday)
        weekday.subtract_days(23)
        print(weekday)
        weekday = Weeker('Monday')
    except WeekDayError:
        print("Sorry, I can't serve your request.")
