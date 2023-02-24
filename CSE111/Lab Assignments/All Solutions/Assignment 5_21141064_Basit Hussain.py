# Task 01

class Marks:
    def __init__(self, mark):
        self.mark = mark
        
    def __add__(self, other):
        return Marks(self.mark + other.mark)
        


Q1 = Marks(int(input("Quiz 1 (out of 10): ")))
Q2 = Marks(int(input("Quiz 2 (out of 10): ")))
Lab = Marks(int(input("Lab (out of 30): ")))
Mid = Marks(int(input("Mid (out of 20): ")))
Final = Marks(int(input("Final (out of 30): ")))
total = Q1 + Q2 + Lab + Mid + Final
print("Total marks: {}".format(total.mark))



# Task 02

class Teacher:
    def __init__(self, name, dep):
        self.__name = name
        self.__dep = dep
        self.__pri = []
    def addCourse(self, c):
        self.__pri.append(c.courses)
    def printDetail(self):
        print("====================================")
        print("Name: ", self.__name)
        print("Department: ", self.__dep)
        print("List of courses")
        print("====================================")
        for i in self.__pri:
            print(i)
        print("====================================")
            
            
class Course:
    def __init__(self, courses):
        self.courses = courses
        
        
t1 = Teacher("Saad Abdullah", "CSE")
t2 = Teacher("Mumit Khan", "CSE")
t3 = Teacher("Sadia Kazi", "CSE")
c1 = Course("CSE 110 Programming Language I")
c2 = Course("CSE 111 Programming Language-II")
c3 = Course("CSE 220 Data Structures")
c4 = Course("CSE 221 Algorithms")
c5 = Course("CCSE 230 Discrete Mathematics")
c6 = Course("CSE 310 Object Oriented Programming")
c7 = Course("CSE 320 Data Communications")
c8 = Course("CSE 340 Computer Architecture")
t1.addCourse(c1)
t1.addCourse(c2)
t2.addCourse(c3)
t2.addCourse(c4)
t2.addCourse(c5)
t3.addCourse(c6)
t3.addCourse(c7)
t3.addCourse(c8)
t1.printDetail()
t2.printDetail()
t3.printDetail()



# Task 3

class Team:
    def __init__(self, name = None):
        self.__name = name
        self.__list = []
        
    def setName(self, new_name):
        if self.__name == None:
            self.__name = new_name
    def addPlayer(self, p):
        self.__list.append(p.players)
        
    def printDetail(self):
        print("====================================")
        print("Team: ", self.__name)
        print("List of Players:")
        print(self.__list)
        print("====================================")
    
    
    
class Player:
    def __init__(self, players):
        self.players = players


b = Team()
b.setName('Bangladesh')
mashrafi = Player("Mashrafi")
b.addPlayer(mashrafi)
tamim = Player("Tamim")
b.addPlayer(tamim)
b.printDetail()
a = Team("Australia")
ponting = Player("Ponting")
a.addPlayer(ponting)
lee = Player("Lee")
a.addPlayer(lee)
a.printDetail()



#Task 4

class Color:
    def __init__(self, clr):
        self.clr = clr
        
    def __add__(self, other):
        self.clr = self.clr + other.clr
        if self.clr == "redyellow" or self.clr == "yellowred":
            self.clr = "Orange"
        elif self.clr == "redblue" or self.clr == "bluered":
            self.clr = "Violet"
        elif self.clr == "yellowblue" or self.clr == "yellowblue":
            self.clr = "Green"
            
        return Color(self.clr)
    
C1 = Color(input("First Color: ").lower())
C2 = Color(input("Second Color: ").lower())
C3 = C1 + C2
print("Color formed:", C3.clr)



# Task 5

import math

class Circle:
    def __init__(self, Radius):
        self.__radius = Radius
        
        
    def getRadius(self):
        return self.__radius
    
    def area(self):
        return   math.pi * self.__radius**2
    
    def __add__(self, other):
        return Circle(self.__radius + other.__radius)
    
    
    
c1 = Circle(4)
print("First circle radius:" , c1.getRadius())
print("First circle area:" ,c1.area())
c2 = Circle(5)
print("Second circle radius:" ,c2.getRadius())
print("Second circle area:" ,c2.area())
c3 = c1 + c2
print("Third circle radius:" ,c3.getRadius())
print("Third circle area:" ,c3.area())



# Task 6

class Triangle:
    def __init__(self, base, height):
        self.__base = base
        self.__height = height
        
    def getBase(self):
        return self.__base
    def setBase(self, base):
        self.__base = base
        return self.__base
    
    def getHeight(self):
        return self.__height
    def setHeight(self, height):
        self.__height = height
        return self.__height
    
    def area(self):
        self.area = (self.__base * self.__height) / 2
        return self.area
    
    def __sub__(self, other):
        new_b = self.__base - other.__base
        new_h = self.__height - other.__height
        return Triangle(new_b, new_h)
    
    
    
t1 = Triangle(10, 5)
print("First Triangle Base:" , t1.getBase())
print("First Triangle Height:" , t1.getHeight())
print("First Triangle area:" ,t1.area())
t2 = Triangle(5, 3)
print("Second Triangle Base:" , t2.getBase())
print("Second Triangle Height:" , t2.getHeight())
print("Second Triangle area:" ,t2.area())
t3 = t1 - t2
print("Third Triangle Base:" , t3.getBase())
print("Third Triangle Height:" , t3.getHeight())
print("Third Triangle area:" ,t3.area())



# task 7

class Dolls:
    def __init__(self, doll, price):
        self.__doll = doll
        self.__price = price
        
    def detail(self):
        return f"Doll: {self.__doll} \nTotal price: {self.__price} taka" 
    
    def __gt__(self, other):
        if self.__price > other.__price:
            return (True)
        else:
            return (False)
        
    def __add__(self, other):
        doll = self.__doll+ " " + other.__doll
        price = self.__price + other.__price

        return Dolls(doll, price)
    
    
obj_1 = Dolls("Tweety", 2500)
print(obj_1.detail())
if obj_1 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")
print("=========================")
obj_2 = Dolls("Daffy Duck", 1800)
print(obj_2.detail())
if obj_2 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")
print("=========================")
obj_3 = Dolls("Bugs Bunny", 3000)
print(obj_3.detail())
if obj_3 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")
print("=========================")
obj_4 = Dolls("Porky Pig", 1500)
print(obj_4.detail())
if obj_4 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")
print("=========================")
obj_5 = obj_2 + obj_3
print(obj_5.detail())
if obj_5 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")
    
    
    
    
# Task 8

class Coordinates:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        
    
    def detail(self):
        return '({},{})'.format(self.__x, self.__y)
        
        
    def __sub__(self, other):
        a = self.__x - other.__x
        b = self.__y - other.__y
        return Coordinates(a, b)
        
    def __mul__(self, other):
        a = self.__x * other.__x
        b = self.__y * other.__y
        return Coordinates(a, b)
        
    def __eq__(self, other):
        if self.__x == other.__x and  self.__y == other.__y:
            return "The calculated coordinates are the same."
        else:
            return "The calculated coordinates are NOT the same."

        
        
p1 = Coordinates(int(input()),int(input()))
p2 = Coordinates(int(input()),int(input()))
p4 = p1 - p2
print(p4.detail())
p5 = p1 * p2
print(p5.detail())
point_check = (p4 == p5)
print(point_check)



# Task 9

class Test:
    def __init__(self):
        self.sum = 0
        self.y = 0
    def methodA(self):
        x=0
        y =0
        y = y + 7
        x = y + 11
        self.sum = x + y
        print(x , y, self.sum)
    def methodB(self):
        x = 0
        self.y = self.y + 11
        x = x + 33 + self.y
        self.sum = self.sum + x + self.y
        print(x , self.y, self.sum)
        
        
t1 = Test()
t1.methodA()
t1.methodA()
t1.methodB()
t1.methodB()



class Test3:
    def __init__(self):
        self.sum, self.y = 0, 0
    def methodA(self):
        x, y = 2, 3
        msg = [0]
        msg[0] = 3
        y = self.y + msg[0]
        self.methodB(msg, msg[0])
        x = self.y + msg[0]
        self.sum = x + y + msg[0]
        print(x, y, self.sum)
    def methodB(self, mg2, mg1):
        x = 0
        self.y = self.y + mg2[0]
        x = x + 33 + mg1
        self.sum = self.sum + x + self.y
        mg2[0] = self.y + mg1
        mg1 = mg1 + x + 2
        print(x, self.y, self.sum)
        
        
t3 = Test3()
t3.methodA()
t3.methodA()
t3.methodA()
t3.methodA()
t3.methodA()



# Task 11
class Test4:
    def __init__(self):
        self.sum, self.y = 0, 0
    def methodA(self):
        x, y = 0, 0
        msg = [0]
        msg[0] = 5
        y = y + self.methodB(msg[0])
        x = y + self.methodB(msg, msg[0])
        self.sum = x + y + msg[0]
        print(x, y, self.sum)
    def methodB(self, *args):
        if len(args) == 1:
            mg1 = args[0]
            x = 0
            y = 0
            y = y + mg1
            x = x + 33 + mg1
            self.sum = self.sum + x + y
            self.y = mg1 + x + 2
            print(x, y, self.sum)
            return y
        else:
            mg2, mg1 = args
            x = 0
            self.y = self.y + mg2[0]
            x = x + 33 + mg1
            self.sum = self.sum + x + self.y
            mg2[0] = self.y + mg1
            mg1 = mg1 + x + 2
            print(x, self.y, self.sum)
            return self.sum
        
        
t3 = Test4()
t3.methodA()
t3.methodA()
t3.methodA()
t3.methodA()
t3.methodA()
