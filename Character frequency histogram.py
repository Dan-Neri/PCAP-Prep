"""
A text file contains some text (nothing unusual) but we need to know how
often (or how rare) each letter appears in the text. Such an analysis 
may be useful in cryptography, so we want to be able to do that in 
reference to the Latin alphabet.

Your task is to write a program which:

  - asks the user for the input file's name;
  - reads the file (if possible) and counts all the Latin letters 
    (lower- and upper-case letters are treated as equal)
  - prints a simple histogram in alphabetical order (only non-zero 
    counts should be presented)

Create a test file for the code, and check if your histogram contains 
valid results.

Assuming that the test file contains just one line filled with:
aBc

samplefile.txt

the expected output should look as follows:
a -> 1
b -> 1
c -> 1

output

Tip: We think that a dictionary is a perfect data collection medium for 
storing the counts. The letters may be keys while the counters can be 
values.
"""
from os import strerror

class Solution:
    #Strategy: 
        #1. Prompt the user to enter the name of the file to read.
        #2. Try to open the specified file catching any exceptions that
            #might be raised.
        #3. Create an empty dictionary, hist, to store the counts of all
            #letters.
        #4. Read from the stream one character at a time.
        #5. If it's a Latin letter, add the letter to hist with a count
            #of 1 or increment the count if it's already in hist.
        #6. Close the stream when the end of the file is reached and
            #print hist.

    #Time complextiy: O(N) N = number of characters in the file
    #Space complexity: O(1)
    def countLetters(self):
        file = input("Enter the name of the file to read: ")
        try:
            stream = open(file, 'rt', encoding = 'utf-8')
        except Exception as e:
            print("Unable to open file:", strerror(e.errno))
            exit(e.errno)
        hist = {}
        ch = stream.read(1)
        while ch != '':
            ch = ch.lower()
            if ord('a') <= ord(ch) and ord(ch) <= ord('z'):
                if ch in hist:
                    hist[ch] += 1
                else:
                    hist[ch] = 1
            ch = stream.read(1)
        for letter, count in hist.items():
            print(letter, '->', count)
        stream.close()
        
if __name__ == "__main__":
    test = Solution()
    test.countLetters()