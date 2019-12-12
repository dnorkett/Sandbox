class Coordinate(object):
    #Object parent is most basic type in Python
    #Data attributes - other objects that make up the class. Numbers, etc.
    def __init__(self, x, y):
        #When you first create an object of this type, call this function. Creates an instance
        #Self is a parameter that represents particular instance of this class.
        self.x = x
        self.y = y

    # Uninformative print representation by default, memory location
    # Python calls the __str__ method when used with print on your class object
    # You get to choose what it shows
    def __str__(self):
        return "<"+str(self.x)+","+str(self.y)+">"

    #Tell Python how to add two objects. Can also do for subtraction, length etc.
    def __add__(self, other):
        return "<"+str(self.x + other.x)+","+str(self.y+other.y)+">"

    #Methods - procedural attributes - functions that work within the class, how to interact with the object
    #Other than self and dot notation, behave similarly to functions (take params, do operations, return)
    def distance(self, other):
        x_diff_sq = (self.x - other.x)**2
        y_diff_sq = (self.y - other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5

#Calls Init. Sets self equal to c, origin. Creates X and Y attributes for object.
c = Coordinate(3,4)
zero = Coordinate(1,1)

#Data attributes of an instance are called instance variables
print(c.x, ",",c.y)
print(zero.x," ",zero.y)

#These two produce the same result. Top method is preferred
print(c.distance(zero))
print(Coordinate.distance(c,zero))

print(type(c))
print(c)
print(isinstance(c,Coordinate))

#Uses the __add__ method to add two Coordinate types together
print(c+zero)

print("*" * 100)

class Fraction(object):
    def __init__(self,numerator, denominator):
        asset type(numerator) == int and type(denominator) == int
        self.numerator = numerator
        self.denominator = denominator
    def __str__(self):
        return str(self.numerator)+"/"+str(self.denominator)
    def __add__(self, other):
        return str((self.numerator*other.denominator) + (self.denominator*other.numerator)) + "/" + str(self.denominator*other.denominator)
    def __sub__(self, other):
        return str((self.numerator*other.denominator) - (self.denominator*other.numerator)) + "/" + str(self.denominator*other.denominator)

fracTestA=Fraction(3,4)
fracTestB=Fraction(1,4)
print(fracTestA)
print(fracTestB)
print(fracTestA + fracTestB)
print(fracTestA - fracTestB)

