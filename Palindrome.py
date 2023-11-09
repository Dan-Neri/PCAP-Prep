"""
Your task is to write a program which:

    asks the user for some text;
    checks whether the entered text is a palindrome, and prints result.

Note:

    assume that an empty string isn't a palindrome;
    treat upper- and lower-case letters as equal;
    spaces are not taken into account during the check - treat them as 
	non-existent;
    there are more than a few correct solutions - try to find more than 
	one.

Test your code using the data we've provided.
Test data

Sample input:
Ten animals I slam in a net

Sample output:
It's a palindrome


Sample input:
Eleven animals I slam in a net

Sample output:
It's not a palindrome

"""
from math import floor

class Solution:
    #Strategy:
        #1. Create a reversed copy of the sring.
        #2. Compare each letter of the strings.
        #3. Return False if you reach a character that doesn't match.
        #4. Return True if you reach the end of the strings.

    #Time complextiy: O(N) N = len(message)
    #Space complexity: O(N)
    def palindromeReverse(self, message):
        if message:
            message = message.replace(' ', '')
        else:
            return False
        rMessage = ''
        for i in range(len(message)):
            rMessage += message[-(i+1)]
        for i in range(len(message)):
            if message[i].lower() != rMessage[i].lower():
                return False
        return True

    #Strategy:
        #1. Slice the string in half creating a second string containg
            #the end of the original string
        #2. Iterate through the second string comparing the last
            #character to the first character of the original string
        #3. Return False if they don't match
        #4. Return True if you reach the end of the second string

    #Time complextiy: O(N)
    #Space complexity: O(N)
    def palindromeSlice(self, message):
        if message:
            message = message.replace(' ', '')
        else:
            return False
        messageBack = message[floor(len(message)/2):]
        for i in range(len(messageBack)):
            if message[i].lower() != messageBack[-(i+1)].lower():
                return False
        return True
        
    #Strategy:
        #1. Iterate through the string.
        #2. Keep track of 2 pointers. One starting at the front and
            #moving forward and another starting at the end and moving
            #backwards.
        #3. Compare the characters at each index and return False if
            #they don't match.
        #4. Return True if you get through at least half the string

    #Time complextiy: O(N)
    #Space complexity: O(1)
    def palindrome(self, message):
        if message:
            message = message.replace(' ', '')
        else:
            return False
        for i in range(floor(len(message)/2)):
            if message[i].lower() != message[-(i+1)].lower():
                return False
        return True

if __name__ == "__main__":
    test = Solution()
    message = input("Please enter some text: ")
    results = []
    results.append(test.palindromeReverse(message))
    results.append(test.palindromeSlice(message))
    results.append(test.palindrome(message))
    #results.append(test.palindrome("Ten animals I slam in a net"))
    #results.append(test.palindrome("Eleven animals I slam in a net"))
    
    for result in results:
        if result:
            print("It's a palindrome")
        else:
            print("It's not a palindrome")