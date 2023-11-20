"""
Now we're going to embed the Point class (see 'Points on a Plane.py') 
inside another class. Also, we're going to put three points into one 
class, which will let us define a triangle. How can we do it?

The new class will be called Triangle and this is the list of our 
expectations:

  - the constructor accepts three arguments - all of them are objects of
    the Point class;
  - the points are stored inside the object as a private list;
  - the class provides a parameterless method called perimeter(), which 
    calculates the perimeter of the triangle described by the three 
    points; the perimeter is a sum of all legs' lengths (we mention it 
    for the record, although we are sure that you know it perfectly 
    yourself.)

Expected output

3.414213562373095

"""

import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y
        
    def distance_from_xy(self, x, y):
        return math.hypot(x - self.__x, y - self.__y)

    def distance_from_point(self, point):
        return math.hypot(point.getx() - self.__x, point.gety() - self.__y)


class Triangle:
    #Time complextiy: O(1)
    #Space complexity: O(1)
    def __init__(self, vertice1, vertice2, vertice3):
        self.__vertices = []
        self.__vertices.append(vertice1)
        self.__vertices.append(vertice2)
        self.__vertices.append(vertice3)
        
    #Strategy:
        #1. Use the distance_from_point() method from the point class to
            #find the length of each side of the triangle.
        #2. Add the length of each side to find the perimeter.
        #3. Return the result.
    #Time complextiy: O(1)
    #Space complexity: O(1)
    def perimeter(self):
        p1 = self.__vertices[0]
        p2 = self.__vertices[1]
        p3 = self.__vertices[2]
        side1 = p1.distance_from_point(p2)
        side2 = p2.distance_from_point(p3)
        side3 = p3.distance_from_point(p1)
        return side1 + side2 + side3

if __name__ == "__main__":
    triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
    print(triangle.perimeter())