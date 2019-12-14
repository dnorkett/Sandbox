import random

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
        assert type(numerator) == int and type(denominator) == int
        self.numerator = numerator
        self.denominator = denominator
    def __str__(self):
        return str(self.numerator)+"/"+str(self.denominator)
    def __add__(self, other):
        return str((self.numerator*other.denominator) + (self.denominator*other.numerator)) + "/" + str(self.denominator*other.denominator)
    def __sub__(self, other):
        return str((self.numerator*other.denominator) - (self.denominator*other.numerator)) + "/" + str(self.denominator*other.denominator)
    def __float__(self):
        return self.numerator / self.denominator
    def inverse(self):
        return Fraction(self.denominator, self.numerator)

fracTestA=Fraction(3,4)
fracTestB=Fraction(1,4)

print(fracTestA)
print(fracTestB)

print(fracTestA + fracTestB)
print(fracTestA - fracTestB)

print(float(fracTestA))
print(float(fracTestB))

print(fracTestA.inverse())

print("*" * 100)


#Class Animal is the parent class / super class
class Animal(object):
    def __init__(self,age):
        self.age = age
        self.name = None
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_new_age(self, new_age):
        self.age = new_age
    def set_name(self, newname=""):
        self.name = newname
    def __str__(self):
        return "animal:"+str(self.name)+":"+str(self.age)

some_animal=Animal(12)
print(some_animal)
some_animal.set_name("Bob")
print(some_animal)
print("*" * 100)


#Class Cat is a child class of Animal. Inherits all data objects and methods
#__init__ not missing, it's using Animal's. Also inherits get_age, get_name etc.
class Cat(Animal):
    def speak(self):
        print("Meow!")
    def __str__(self):
        return "cat:"+str(self.name)+":"+str(self.age)

some_cat=Cat(3)
print(some_cat)
some_cat.speak()
some_cat.set_name("Mittens")
print(some_cat)
print("*" * 100)


#Calls Animal init method to initialize name and data attributes since it's already done in code
#Can do other things in init, like set variables, call methods etc
#Also creates new methods that are specific to Person sub-class
class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self,age)
        self.set_name(name)
        self.friends=[]
    def get_friends(self):
        return self.friends
    def add_friend(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)
    def speak(self):
        print("Hello!")
    def age_diff(self,other):
        diff = self.age - other.age
        print (abs(diff), "year difference")
    def __str__(self):
        return "person:"+str(self.name)+":"+str(self.age)

some_person = Person("James", 12)
print(some_person)
some_person.speak()
print(some_person.get_friends())
some_person.add_friend("Abby")
some_person.add_friend("Ben")
print(some_person.get_friends())

other_person = Person("Ryan", 10)
some_person.age_diff(other_person)
print("*" * 100)


#Subclass of Person, which is a subclass of Animal
#Inherits Person and Animal attributes
class Student(Person):
    def __init__(self, name, age, major=None):
        Person.__init__(self, name, age)
        self.major = major
    def change_major(self, major):
        self.major = major
    def speak(self):
        r = random.random()
        if r < 0.25:
            print("I have homework")
        elif .25 <= r < 0.5:
            print("I need sleep")
        elif .5 <= r < 0.75:
            print("I should eat")
        else:
            print("I am watching TV")
    def __str__(self):
        return "student:"+str(self.name)+":"+str(self.age)+":"+str(self.major)

don = Student('Don', 35)
print(don)
don.change_major('CS')
print(don)
don.speak()
print("*" * 100)

#Instance variables - self.name, self.age etc.
#Common across all instances of the class. Value different for all instances
#Class variables - values are shared between all instances of a class
class Rabbit(Animal):
    tag = 1
    def __init__(self, age, parent1=None, parent2=None):
        Animal.__init__(self, age)
        self.parent1 = parent1
        self.parent2 = parent2
        #assigning instance variable to class variable
        self.rid = Rabbit.tag
        #tag used to give unique id to each new rabbit instance
        Rabbit.tag +=1
    def get_rid(self):
        #zfill pads start of a string with 0s to always be X digits long
        return str(self.rid).zfill(3)
    def get_parent1(self):
        return self.parent1
    def get_parent2(self):
        return self.parent2
    def __add__(self, other):
        #returning object of same type as this class
        #From init - 0 is age, self is parent1, other is parent2
        return Rabbit(0, self, other)
    def __eq__(self, other):
        parents_same = self.parent1.rid == other.parent1.rid and self.parent2.rid == other.parent2.rid
        parents_opposite = self.parent2.rid == other.parent1.rid and self.parent1.rid == other.parent2.rid
        return parents_same or parents_opposite

print("*" * 100)
rab1 = Rabbit(2)
rab2 = Rabbit(2)
