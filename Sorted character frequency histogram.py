"""
The previous code (See Character frequency histogram.py) needs to be 
improved. It's okay, but it has to be better.

Your task is to make some amendments, which generate the following 
results:

  - the output histogram will be sorted based on the characters' 
    frequency (the bigger counter should be presented first)
  - the histogram should be sent to a file with the same name as the 
    input one, but with the suffix '.hist' (it should be concatenated to
    the original name)

Assuming that the input file contains just one line filled with:
cBabAa

samplefile.txt

the expected output should look as follows:
a -> 3
b -> 2
c -> 1

output

Tip: Use a lambda to change the sort order.
"""

class Solution:
    #Strategy:
        #1. Start with the code from the previous problem.
        #2. Open a second stream to write the output by appending 
            #'.hist' to the given filename
        #2. Sort hist in decending order according to frequency before
            #printing it.
        #3. Write the output to both a file and the screen.
    #Time complextiy: 
    #Space complexity: 
    def countLetters(self):
        file = input("Enter the name of the file to read: ")
        oFile = file + '.hist'
        try:
            stream = open(file, 'rt', encoding = 'utf-8')
        except Exception as e:
            print(f"Unable to open {file}:", strerror(e.errno))
            exit(e.errno)
        try:
            output = open(oFile, 'wt', encoding = 'utf-8')
        except Exception as e:
            print(f"Unable to open {oFile}:", strerror(e.errno))
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
        for x in sorted(hist, key = lambda x: hist[x], reverse = True):
            line = "{0} -> {1}\n".format(x, hist[x])
            print(line, end = '')
            output.write(line)
        stream.close()
        output.close()
        
if __name__ == "__main__":
    test = Solution()
    test.countLetters()
