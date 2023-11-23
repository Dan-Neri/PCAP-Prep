"""
Prof. Jekyll conducts classes with students and regularly makes notes in
a text file. Each line of the file contains three elements: the 
student's first name, the student's last name, and the number of point 
the student received during certain classes.

The elements are separated with white spaces. Each student may appear 
more than once inside Prof. Jekyll's file.

The file may look as follows:
John	Smith	5
Anna	Boleyn	4.5
John	Smith	2
Anna	Boleyn	11
Andrew	Cox	    1.5

samplefile.txt

Your task is to write a program which:

  - asks the user for Prof. Jekyll's file name;
  - reads the file contents and counts the sum of the received points 
    for each student;
  - prints a simple (but sorted) report, just like this one:

Andrew Cox 	 1.5
Anna Boleyn  15.5
John Smith 	 7.0

output

Note:

  - your program must be fully protected against all possible failures: 
    the file's non-existence, the file's emptiness, or any input data 
    failures; encountering any data error should cause immediate program
    termination, and the erroneous should be presented to the user;
  - implement and use your own exceptions hierarchy - we've presented it
    in the editor; the second exception should be raised when a bad line
    is detect, and the third when the source file exists but is empty.

Tip: Use a dictionary to store the students' data.
"""
from os import strerror

class StudentsDataException(Exception):
    pass


class BadLine(StudentsDataException):
    def __init__(self, line, msg):
        StudentsDataException.__init__(self, msg)
        self.line = ''
        for x in line:
            self.line += x + ' '

class FileEmpty(StudentsDataException):
    def __init__(self, msg):
        StudentsDataException.__init__(self, msg)
        self.line = ''


class Solution:
    #Strategy:
        #1. Prompt the user for the name of the file.
        #2. Open a stream to read from the file.
        #3. Read the first line of the file.
        #4. If the file is empty raise the FileEmpty exception.
        #5. Split the line into a list of 3 elements.
        #6. Attempt to convert the 3rd element into an float and add it to
            #the student's current point total.
        #7. Raise the BadLine exception if this instruction fails.
        #8. Iterate through the sorted dictionary and print each 
            #student's score.

    #Time complextiy: O(N) N = number of lines in the file
    #Space complexity: O(N) 
    def calculateScores(self):
        msg = "Enter the name of the file containing the student's scores: "
        file = input(msg)
        scores = {}
        try:
            stream = open(file, 'r', encoding = 'UTF-8')
        except Exception as e:
            print("Unable to open file", strerror(e.errno))
            exit(e.errno)
        try:
            line = stream.readline().split()
            if len(line) == 0:
                raise FileEmpty("The file is empty")
            elif len(line) != 3:
                raise BadLine(line, "This line is invalid")
        except FileEmpty as e:
            print(e)
        except BadLine as e:
            print(e, ': ', e.line)
        except Exception as e:
            print("Unknown error: ", strerror(e))
            exit(e.errno)
        try:
            while len(line) != 0:
                name = line[0] + ' ' + line[1]
                if name in scores:
                    scores[name] += float(line[2])
                else:
                    scores[name] = float(line[2])
                line = stream.readline().split()
        except ValueError as e:
            try:
                raise BadLine(line, "The score on this line is invalid")
            except BadLine as e:
                print(e, ': ', e.line)
        except Exception as e:
            print("Unknown error: ", strerror(e))
            exit(e.errno)
        for x in sorted(scores):
            print("{0:15s}{1:.1f}".format(x, scores[x]))
    
    
if __name__ == "__main__":
    test = Solution()
    test.calculateScores()