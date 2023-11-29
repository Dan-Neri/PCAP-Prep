"""
Write a program that creates a datetime object for November 4, 2020 , 
14:53:00. The object created should call the strftime method with the 
appropriate format to display the following result:

2020/11/04 14:53:00
20/November/04 14:53:00 PM
Wed, 2020 Nov 04
Wednesday, 2020 November 04
Weekday: 3
Day of the year: 309
Week number of the year: 44

expected output

Note: Each result line should be created by calling the strftime method 
with at least one directive in the format argument.
"""
from datetime import datetime
 
if __name__ == "__main__":
    d1 = datetime(2020, 11, 4, 14, 53, 0)
    print(d1.strftime("%Y/%m/%d %H:%M:%S"))
    print(d1.strftime("%y/%B/%d %H:%M:%S %p"))
    print(d1.strftime("%a, %Y %b %d"))
    print(d1.strftime("%A, %Y %B %d"))
    print(d1.strftime("Weekday: %u"))
    print(d1.strftime("Day of the year: %j"))
    print(d1.strftime("Week number of the year: %U"))
