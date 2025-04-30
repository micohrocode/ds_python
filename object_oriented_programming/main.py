# a class is a data type
# an object is an instance of a class
class Vector:
    def __init__(self,x ,y):
        self.x = x
        self.y = y

    # functions in a class are called methods
    def norm(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    # __ are magic methods
    def __add__(self, other):
        newx = self.x + other.x
        newy = self.y + other.y
        return Vector(newx,newy)
    
    # implement how a vector should be printed
    def __str__(self):
        return "(%f,%f)"%(self.x,self.y)
    
# underscores mark what should be a private method
# often for accessing

class Polygon:
    def __init__(self, sides, points):
        self._sides = sides
        self._points = list(points)
        if len(self._points) != self._sides:
            raise ValueError("Wrong number of points")
        
    def sides(self):
        return self._sides

# these classes inherit from Polygon
# Triangle "is a" Polygon
class Triangle(Polygon):
    def __init__(self, sides, points):
        super().__init__(3, points)
    
    def __str__(self):
        return "I am a triangle"
    
class Square(Polygon):
    def __init__(self, sides, points):
        super().__init__(4, points)
    
    def __str__(self):
        return "I am a Square"
    
# Composition, one class stores an instance
# of another class
# "has a"
class MyLimitedList:
    def __init__(self):
        # list class used here
        self._L = []
    
    def append(self, item):
        self._L.append(item)

    def __getitem__(self, index):
        return self._L[index]