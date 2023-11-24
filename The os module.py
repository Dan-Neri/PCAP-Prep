"""
It goes without saying that operating systems allow you to search for 
files and directories. While studying this part of the course, you 
learned about the functions of the os module, which have everything you 
need to write a program that will search for directories in a given 
location.

To make your task easier, we have prepared a test directory structure 
for you:

[tree]
    --[c]
        --[other_courses]
            --[cpp]
            --[python]
    --[cpp]
        --[other_courses]
            --[c]
            --[python]
    --[python]
        --[other_courses]
            --[c]
            --[cpp]


Your program should meet the following requirements:

  - Write a function or method called find that takes two arguments 
    called path and dir. The path argument should accept a relative or 
    absolute path to a directory where the search should start, while 
    the dir argument should be the name of a directory that you want to 
    find in the given path. Your program should display the absolute 
    paths if it finds a directory with the given name.
  - The directory search should be done recursively. This means that the
    search should also include all subdirectories in the given path.

Example input:
path="./tree", dir="python"

Example output:
.../tree/python
.../tree/cpp/other_courses/python
.../tree/c/other_courses/python
"""
import os

class Solution:
    #Note: This method is used to create the directory structure
        #given in the problem description.
    #Time complextiy: O(N) N = number of directories in direct and path
    #Space complexity: O(N)
    def makeDirs(self, direct: str, path: str = './'):
        direct = direct.replace('\\', '/').strip('/ ')
        path = path.replace('\\', '/').strip('/ ')
        try:
            os.makedirs(f'{path}/{direct}')
            print(f'creating {path}/{direct}')
        except FileExistsError as e:
            print(f'{path}/{direct} already exists')
        except Exception as e:
            print(e)
            exit(e.errno)
            
    #Strategy: T
        #1. Try to change the working directory to the path given.
        #2. Set the path to the working directory in order to change any
            #relative path to a full path.
        #3. Iterate through the contents of the working directory.
        #4. If a subdirectory is found, call self.find() on this
            #directory.
        #5. Check if a directory matching the tartget, direct, is found.
        #6. If it is, print the full path of that directory.
        #7. Make sure that the working directory is set back to the
            #current directory before checking the next file in this
            #directory.
            

    #Time complextiy: O(N * M) N = number sub directories in path
        #M = number of files and directories in each directory
    #Space complexity: O(1)
    def find(self, path: str, direct: str):
        try:
            os.chdir(path)
            path = os.getcwd()
            contents = os.listdir()
            for fd in contents:
                if '.' not in fd:
                    self.find(f'{path}/{fd}', direct)
                if fd == direct:
                    print(f'{path}/{fd}')
                os.chdir(path)
                
        except Exception as e:
            print(e)
            exit(e.errno)
        
    
if __name__ == "__main__":
    test = Solution()
    #Create the initial tree structure
    test.makeDirs('cpp', 'tree/c/other_courses')
    test.makeDirs('python', 'tree/c/other_courses')
    test.makeDirs('c', 'tree/cpp/other_courses')
    test.makeDirs('python', 'tree/cpp/other_courses/')
    test.makeDirs('c', 'tree/python/other_courses')
    test.makeDirs('cpp', 'tree/python/other_courses/')
    #Check test case
    test.find('./tree', 'python')