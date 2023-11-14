"""
Your task is to write a function able to input integer values and to 
check if they are within a specified range.

The function should:

  - accept three arguments: a prompt, a low acceptable limit, and a high 
    acceptable limit;
  - if the user enters a string that is not an integer value, the 
    function should emit the message Error: wrong input, and ask the 
    user to input the value again;
  - if the user enters a number which falls outside the specified range,
    the function should emit the message Error: the value is not within 
    permitted range (min..max) and ask the user to input the value 
    again;
  - if the input value is valid, return it as a result.

Test data

Test your code carefully.

This is how the function should react to the user's input:
Enter a number from -10 to 10: 100
Error: the value is not within permitted range (-10..10)
Enter a number from -10 to 10: asd
Error: wrong input
Enter number from -10 to 10: 1
The number is: 1
"""

class Solution:
    #Strategy:
        #1. Create a while loop that asks for the user to input a number
            #in the valid range.
        #2. Cast the input as an int and use assert to check if it is in
            #the correct range.
        #3. If a ValueError is raised, then the int conversion failed.
        #4. If an AssertionError is raised, then the value was not in
            #the correct range.
        #5. End the loop and return the provided number if no exception
            #was raised.

    #Time complextiy: O(1)
    #Space complexity: O(1)
    def read_int(self, prompt: str, min: int, max: int):
        invalid = True
        while invalid:
            num = input(f"Enter a number from {min} to {max}: ")
            try:
                assert (min <= int(num) and max >= int(num))
                invalid = False
            except ValueError:
                print("Error: wrong input")
            except AssertionError:
                print("Error: the value is not within permitted " + 
                      f"range({min}..{max})")
        return num
        
if __name__ == "__main__":
    test = Solution()
    v = test.read_int("Enter a number from -10 to 10: ", -10, 10)
    print("The number is:", v)