"""
Some say that the Digit of Life is a digit evaluated using somebody's 
birthday. It's simple - you just need to sum all the digits of the date.
If the result contains more than one digit, you have to repeat the 
addition until you get exactly one digit. For example:

  - 1 January 2017 = 2017 01 01
  - 2 + 0 + 1 + 7 + 0 + 1 + 0 + 1 = 12
  - 1 + 2 = 3

3 is the digit we searched for and found.

Your task is to write a program which:

  - asks the user her/his birthday (in the format YYYYMMDD, or YYYYDDMM,
	or MMDDYYYY - actually, the order of the digits doesn't matter)
  - outputs the Digit of Life for the date.

Test your code using the data we've provided.
Test data

Sample input:
19991229

Sample output:
6


Sample input:
20000101

Sample output:
4

"""

class Solution:
    #Strategy:
        #1. Check to make sure that the text entered is in the correct
            #format.
        #2. Change the text into a list of characters.
        #3. Change each character to an int and add them to the result.
        #4. Change the result back into a list of characters.
        #5. If the list contains more than one character, repeat the 
            #addition.
        #6. Return the final result.

    #Time complextiy: O(1)
    #Space complexity: O(1)
    def lifeDigit(self):
        invalid = True
        while invalid:
            message = "Please enter your birthdaty in the form MMDDYY: "
            birthday = input(message)
            if not birthday.isdigit():
                print("Please enter only numbers.")
                continue
            birthday = list(birthday)
            if len(birthday) != 8:
                print("Please enter your birthday in the form MMDDYYYY")
            else:
                invalid = False
        while len(birthday) > 1:
            result = 0
            for char in birthday:
                result += int(char)
            birthday = list(str(result))
        return result
    
if __name__ == "__main__":
    test = Solution()
    print(test.lifeDigit())