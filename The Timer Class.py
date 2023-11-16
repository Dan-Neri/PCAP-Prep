"""
Your class will be called Timer. Its constructor accepts three arguments
representing hours (a value from range [0..23] - we will be using the 
military time), minutes (from range [0..59]) and seconds (from range 
[0..59]).

Zero is the default value for all of the above parameters. There is no 
need to perform any validation checks.

The class itself should provide the following facilities:

  - objects of the class should be "printable", i.e. they should be able
	to implicitly convert themselves into strings of the following form:
	"hh:mm:ss", with leading zeros added when any of the values is less 
	than 10;
  - the class should be equipped with parameterless methods called 
	next_second() and previous_second(), incrementing the time stored 
	inside objects by +1/-1 second respectively.

Use the following hints:

  - all object's properties should be private;
  - consider writing a separate function (not method!) to format the 
	time string.

Complete the template we've provided in the editor. Run your code and 
check whether the output looks the same as ours.

Expected output

23:59:59
00:00:00
23:59:59
"""

class Timer:
    #Time complextiy: O(1)
    #Space complexity: O(1)
    def __init__(self, hours: int = 0, minutes: int = 0, seconds: int = 0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    #Time complextiy: O(1)
    #Space complexity: O(1)
    def __str__(self):
        s = "{:02d}:{:02d}:{:02d}"
        return s.format(self.__hours, self.__minutes, self.__seconds)

    #Time complextiy: O(1)
    #Space complexity: O(1)
    def next_second(self):
        self.__seconds += 1
        if self.__seconds >= 60:
            self.__seconds -= 60
            self.__minutes += 1
        if self.__minutes >= 60:
            self.__minutes -= 60
            self.__hours += 1
        if self.__hours >= 24:
            self.__hours -= 24

    #Time complextiy: O(1)
    #Space complexity: O(1)
    def prev_second(self):
        self.__seconds -= 1
        if self.__seconds < 0:
            self.__seconds += 60
            self.__minutes -= 1
        if self.__minutes < 0:
            self.__minutes += 60
            self.__hours -= 1
        if self.__hours < 0:
            self.__hours += 24


if __name__ == "__main__":
	timer = Timer(23, 59, 59)
	print(timer)
	timer.next_second()
	print(timer)
	timer.prev_second()
	print(timer)