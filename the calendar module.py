"""
During this course, we looked at the Calendar class a bit. Your task is 
to extend its functionality with a new method called 
count_weekday_in_year, which takes a year and a weekday as parameters, 
and then returns the number of occurrences of a specific weekday in the 
year.

Use the following tips:

  - Create a class called MyCalendar that extends the Calendar class;
  - create the count_weekday_in_year method with the year and weekday 
    parameters. The weekday parameter should be a value between 0-6, 
    where 0 is Monday and 6 is Sunday. The method should return the 
    number of days as an integer;
  - in your implementation, use the monthdays2calendar method of the 
    Calendar class.

The following are the expected results:

Sample arguments

year=2019, weekday=0

Expected output

52

Sample arguments

year=2000, weekday=6

Expected output

53

"""
from calendar import Calendar

class MyCalendar(Calendar):
    #Strategy:
        #1. Iterate through every month in the year.
        #2. Iterate through each week in the month returned by 
            #monthdays2calendar().
        #3. Iterate through each day in the week and check if it is partition
            #of the month and the correct day of the week.
        #4. If it is, increment the count.
        #5. return the count after all days of the year have been 
            #checked.

    #Time complextiy: O(1)
    #Space complexity: O(1)
    def count_weekday_in_year(self, year, weekday):
        count = 0
        try:
            assert(1 <= int(year) and 9999 >= int(year))
            assert(0 <= int(weekday) and 6 >= int(weekday))
        except ValueError:
            print("year and weekday must be integers")
        except AssertionError:
            print("year or weekday not valid")
        except Exception as e:
            print(e)
        for i in range(1, 13):
            for week in self.monthdays2calendar(year, i):
                for date, day in week:
                    if date > 0 and day == weekday:
                        count += 1
        return count
    
if __name__ == "__main__":
    test = MyCalendar()
    print(test.count_weekday_in_year(2019, 0))
    print(test.count_weekday_in_year(2000, 6))