"""
The original Caesar cipher shifts each character by one: a becomes b, z 
becomes a, and so on. Let's make it a bit harder, and allow the shifted 
value to come from the range 1..25 inclusive.

Moreover, let the code preserve the letters' case (lower-case letters 
will remain lower-case) and all non-alphabetical characters should 
remain untouched.

Your task is to write a program which:

    asks the user for one line of text to encrypt;
    asks the user for a shift value (an integer number from the range 
	1..25 - note: you should force the user to enter a valid shift value
	(don't give up and don't let bad data fool you!)
    prints out the encoded text. 

Test your code using the data we've provided.
Test data

Sample input:
abcxyzABCxyz 123
2

Sample output:
cdezabCDEzab 123

Sample input:
The die is cast
25

Sample output:
Sgd chd hr bzrs

"""

class Solution:
    #Strategy:
        #1. Prompt the user for the message and the shift
        #2. Check shift for validity
        #3. Create an empty string to store the cipher
        #4. Iterate through the message one character at a time
        #5. Check if the character is an uppercase or lowercase letters
        #6. If it is, do the necessary shift and add the new character
            #to the cipher
        #7. If it is not, just add the character as is to the cipher
        #8. Print the final cipher

    #Time complextiy: O(N) N = len(message)
    #Space complexity: O(N)
    def caesar(self, message, shift):
        try: 
            shift = int(shift)
            if shift <= 0 or shift > 25:
                throw(exception)
        except:
            print("Please enter a number between 1 and 25")
            return 0
        cipher = ''
        for ch in message:
            if ch.isupper():
                code = ord(ch) + shift
                if code > ord('Z'):
                    code -= 26
                cipher += chr(code)
            elif ch.islower():
                code = ord(ch) + shift
                if code > ord('z'):
                    code -= 26
                cipher += chr(code)
            else:
                cipher += ch
        print(cipher)
        return 1
    
if __name__ == "__main__":
    test = Solution()
    message = input("Please enter a message to be encoded: ")
    valid = 0
    while not valid:
        prompt = "Enter a number between 1 and 25 to encode the message: "
        shift = input(prompt)
        valid = test.caesar(message, shift)