#!/usr/bin/env python
# coding: utf-8

# In[29]:


# Practices

class parent:
    def __init__(self):
        print("constructor of p")
    def method1(self):
        print("m1p")
        
    def method2(self):
        print("m2p")
        
class child1(parent):
    def __init__(self):
        print("constructor of c1")
    def method3(self):
        print("m3c1")
        
    def method4(self):
        print("m4c1")
        
class child2(parent):
    def __init__(self):
        print("constructor of c2")
    def method5(self):
        print("m3c2")
        
    def method6(self):
        print("m4c2")
        
        
class grandchild(child1, child2):
    def __init__(self):
        super().__init__()
        print("constructor of gc")
    def method7(self):
        print("m7gc")
        
    def method6(self):
        print("m7gc")
        
p = grandchild()


# In[1]:


# Task 1

class Student:
    def __init__(self, name='Just a student', dept='nothing'):
        self.__name = name
        self.__department = dept
    def set_department(self, dept):
        self.__department = dept
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name = name
    def __str__(self):
        return 'Name: '+self.__name+' Department: '+self.__department
class BBA_Student(Student):
    def __init__(self, name = "default", dept= "BBA"):
        super().__init__(name, dept)
#write your code here
print(BBA_Student())
print(BBA_Student('Humpty Dumpty'))
print(BBA_Student('Little Bo Peep'))


# In[3]:


# Task 2

class Vehicle:
    def __init__(self):
        self.x = 0
        self.y = 0
    def moveUp(self):
        self.y+=1
    def moveDown(self):
        self.y-=1
    def moveRight(self):
        self.x+=1
    def moveLeft(self):
        self.x-=1
    def __str__(self):
        return '('+str(self.x)+' , '+str(self.y)+')'
    
class Vehicle2010(Vehicle):
    

    def moveLowerLeft(self):
        super().moveDown()
        super().moveLeft()
    
    def moveLowerRight(self):
        super().moveDown()
        super().moveRight()
        
    def moveUpperLeft(self):
        super().moveUp()
        super().moveLeft()
    
    def moveUpperRight(self):
        super().moveUp()
        super().moveRight()

        

        
    def equals(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False
        
    
    
#write your code here
print('Part 1')
print('------')
car = Vehicle()
print(car)
car.moveUp()
print(car)
car.moveLeft()
print(car)
car.moveDown()
print(car)
car.moveRight()
print(car)
print('------')
print('Part 2')
print('------')
car1 = Vehicle2010()
print(car1)
car1.moveLowerLeft()
print(car1)
car2 = Vehicle2010()
car2.moveLeft()
print(car1.equals(car2))
car2.moveDown()
print(car1.equals(car2))


# In[24]:


#Task 3
class Tournament:
    def __init__(self,name='Default'):
        self.__name = name
    def set_name(self,name):
        self.__name = name
    def get_name(self):
        return self.__name
    
class Cricket_Tournament(Tournament):
    def __init__(self, name = "Default", number = 0, typee = "No type"):
        super().__init__(name)
        self.number =number
        self.typee=typee

            
    def detail(self):
        return "Cricket Tournament Name: {}\nNumber of teams: {}\nType: {}".format(super().get_name(), self.number, self.typee)
            
class Tennis_Tournament(Tournament):
    def __init__(self, name, number):
        super().__init__(name)
        self.number =number

            
    def detail(self):
        return "Tennis Tournament Name: {}\nNumber of Players: {}".format(super().get_name(), self.number)
            
    
    
#write your code here
ct1 = Cricket_Tournament()
print(ct1.detail())
print("-----------------------")
ct2 = Cricket_Tournament("IPL",10,"t20")
print(ct2.detail())
print("-----------------------")
tt = Tennis_Tournament("Roland Garros",128)
print(tt.detail())


# In[21]:


#Task4
class Product:
    def __init__(self,id, title, price):
        self.__id = id
        self. __title = title
        self. __price = price
    def get_id_title_price(self):
        return "ID: "+str(self.__id)+" Title: "+self.__title+"Price: "+str(self.__price)


#write your code here
class Book(Product):
    def __init__(self, id, title, price, isbn, publisher):
        super().__init__(id, title, price)
        self.isbn =isbn
        self.publisher = publisher
    def printDetail(self):
        return '{}\nISBN: {} Publisher: {}'.format(super().get_id_title_price(),self.isbn,self.publisher)
class CD(Product):
    def __init__(self, id, title, price, band, duration, genre):
        super().__init__(id, title, price)
        self.band = band
        self.duration = duration
        self.genre = genre
    def printDetail(self):
        return '{}\nBand: {} Duration: {}minutes\nGenre: {}'.format(super().get_id_title_price(),self.band,self.duration,self.genre)

    

book = Book(1,"The Alchemist",500,"97806","HarperCollins")
print(book.printDetail())
print("-----------------------")
cd = CD(2,"Shotto",300,"Warfaze",50,"Hard Rock")
print(cd.printDetail())


# In[22]:


#Task 5
class Animal:
    def __init__(self,sound):
        self.__sound = sound
    def makeSound(self):
        return self.__sound

class Printer:
    def printSound(self, a):
        print(a.makeSound())
        
class Cat(Animal):
    def __init__(self, sound):
        super().__init__(sound)
        
class Dog(Animal):
    def __init__(self, sound):
        super().__init__(sound)

        
        
        
#write your code here
d1 = Dog('bark')
c1 = Cat('meow')
a1 = Animal('Animal does not make sound')
pr = Printer()
pr.printSound(a1)
pr.printSound(c1)
pr.printSound(d1)


# In[30]:


#Task 6
class Shape:
    def __init__(self, name='Default', height=0, base=0):
        self.area = 0
        self.name = name
        self.height = height
        self.base = base
    def get_height_base(self):
        return "Height: "+str(self.height)+",Base: "+str(self.base)
#write your code here
class triangle(Shape):
    def calcArea(self):
        self.area = (self.height * self.base) / 2
        
    def printDetail(self):
        return (
            f"Shape name: {self.name}\n"
            + super().get_height_base()
            + f"\nArea: {self.area}"
        )
    
class trapezoid(Shape):
    def __init__(self, name, height, base, s):
        super().__init__(name, height, base)
        self.s = s
    
    def calcArea(self):
        self.area = ((self.base + self.s) / 2) * self.height
        
    def printDetail(self):
        return (
            f"Shape name: {self.name}\n"
            + super().get_height_base()
            + f", Side_A: {self.s}"
            + f"\nArea: {self.area}"
        )
tri_default = triangle()
tri_default.calcArea()
print(tri_default.printDetail())
print('--------------------------')
tri = triangle('Triangle', 10, 5)
tri.calcArea()
print(tri.printDetail())
print('---------------------------')
trap = trapezoid('Trapezoid', 10, 6, 4)
trap.calcArea()
print(trap.printDetail())


# In[10]:


#Task 7
class Football:
    def __init__(self, team_name, name, role):
        self.__team = team_name
        self.__name = name
        self.role = role
        self.earning_per_match = 0
    def get_name_team(self):
        return 'Name: '+self.__name+', Team Name: ' +self.__team
    
    
class Player(Football):
    def __init__(self, team_name, name, role, tg, tp):
        super().__init__(team_name, name, role)
        self.tg = tg
        self.tp = tp
        
    def calculate_ratio(self):
        self.ratio = self.tg / self.tp
        
    def print_details(self):
        earning = (self.tg * 1000) + (self.tp * 10)
        print(super().get_name_team())
        print("Team Role:", self.role)
        print("Total Goal:", self.tg, "Total Played:", self.tp)
        print("Goal Ratio:", self.ratio)
        print(f"Match Earning: {earning}K")
        
class Manager(Football):
    def __init__(self, team_name, name, role, w):
        super().__init__(team_name, name, role)
        self.w = w
        
    def print_details(self):
        earning = self.w * 1000
        print(super().get_name_team())
        print("Team Role:", self.role)
        print("Win:", self.w)
        print(f"Match Earning: {earning}K")
        
        
        
    
#write your code here
player_one = Player('Juventus', 'Ronaldo', 'Striker', 25, 32)
player_one.calculate_ratio()
player_one.print_details()
print('------------------------------------------')
manager_one = Manager('Real Madrid', 'Zidane', 'Manager', 25)
manager_one.print_details()
