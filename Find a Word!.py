"""
Let's play a game. We will give you two strings: one being a word 
(e.g., "dog") and the second being a combination of any characters.

Your task is to write a program which answers the following question: 
are the characters comprising the first string hidden inside the second 
string?

For example:

  - if the second string is given as "vcxzxduybfdsobywuefgas", the 
    answer is yes;
  - if the second string is "vcxzxdcybfdstbywuefsas", the answer is no 
    (as there are neither the letters "d", "o", or "g", in this order)

Hints:

  - you should use the two-argument variants of the pos() functions 
    inside your code;
  - don't worry about case sensitivity.

Test your code using the data we've provided.
Test data

Sample input:

donor
Nabucodonosor

Sample output:
Yes


Sample input:

donut
Nabucodonosor

Sample output:
No

"""

class Solution:
    #Strategy:
        #1. Change the first string into a list.
        #2. Iterate through the list and check if each character is in
            #the second string using find()
        #3. If any character is not in the string, return False
        #4. If you reach the end of the list, return True

    #Time complextiy: O(N)
    #Space complexity: O(1)
    def contained(self, word, chars):
        word = list(word)
        for char in word:
            if chars.find(char) == -1:
                return False
        return True
    
if __name__ == "__main__":
    test = Solution()
    word = 'donor'
    chars = 'Nabucodonosor'
    if test.contained(word, chars):
        print('Yes')
    else:
        print('No')
    word = 'donut'
    chars = 'Nabucodonosor'
    if test.contained(word, chars):
        print('Yes')
    else:
        print('No')
        