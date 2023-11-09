"""
An anagram is a new word formed by rearranging the letters of a word,
using all the original letters exactly once. For example, the phrases
"rail safety" and "fairy tales" are anagrams, while "I am" and "You are"
are not.

Your task is to write a program which:

  - asks the user for two separate texts;
  - checks whether, the entered texts are anagrams and prints the 
	result.

Note:

  - assume that two empty strings are not anagrams;
  - treat upper- and lower-case letters as equal;
  - spaces are not taken into account during the check - treat them as
	non-existent

Test data

Sample input:
Listen
Silent

Sample output:
Anagrams


Sample input:
modern
norman

Sample output:
Not anagrams
"""

class Solution:
    #Strategy:
        #1. Check if either input is empty.
        #2. If it is, return False.
        #3. Remove any spaces from the texts
        #3. Check if the two texts are the same length.
        #4. If they aren't, return False.
        #4. Iterate through the first string one character at a time.
        #5. Starting at the current character until the end of the first
            #text, check if this is equal to text2
        #5. If it is, return True.
        #6. If it isn't, create a substring of text2 by removing the
            #the first character of text1 from it.
        #7. If that character isn't in the second string, return False.
        #8. Otherwise, move to the next character in text1
        #9. If the end of the text is reached, return True

    #Time complextiy: O(N * (N + M)) N = len(text1) M = len(text2)
    #Space complexity: O(N)
    def isAnagram(self, text1, text2):
        if text1 == '' or text2 == '':
            return False
        text1 = text1.replace(' ', '')
        text2 = text2.replace(' ', '')
        if len(text1) != len(text2):
            return False
        for i in range(len(text1)):
            if text1[i:] == text2:
                return True
            index = text2.lower().find(text1[i].lower())
            if  index == -1:
                return False
            else:
                text2 = text2[:index] + text2[index + 1:]
        return True
    
    #Strategy:
        #1. Check if either text is empty.
        #2. If it is, return False.
        #3. Otherwise, split text1 and text2 into lists with each 
            #element containing a character.
        #4. Iterate through the first list and remove each character
            #from the second list.
        #5. If the character is not found in the second list, return
            #False
        #6. After the end of the first list has been reached, if there
            #are more characters in the second list, return False
        #7. Otherwise return True
        
    #Time complextiy: O(N * M)
    #Space complexity: O(N)
    def isAnagramSplit(self, text1, text2):
        if text1 == '' or text2 == '':
            return False
        list1 = []
        list2 = []
        for char in text1:
            if char.isspace():
                continue
            else:
                list1.append(char.lower())
        for char in text2:
            if char.isspace():
                continue
            else:
                list2.append(char.lower())
        for char in list1:
            if char in list2:
                list2.remove(char)
            else:
                return False
        if list2:
            return False
        else:
            return True
            
if __name__ == "__main__":
    test = Solution()
    #text1 = ''
    #text2 = ''
    #text1 = 'Listen'
    #text2 = 'Silent'
    #text1 = 'modern'
    #text2 = 'norman'
    #text1 = '1 0 0 A'
    #text2 = '00a1'
    text1 = input("Please enter a message: ")
    text2 = input("Please enter a second message: ")
    if test.isAnagramSplit(text1, text2):
        print("Anagrams")
    else:
        print("Not anagrams")