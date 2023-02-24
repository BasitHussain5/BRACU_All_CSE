#!/usr/bin/env python
# coding: utf-8

# In[5]:


class Student:
    ID = 0
    def __init__(self, name, department, age, cgpa):
        self.name = name
        self.department = department
        self.age = age
        self.cgpa = cgpa
        Student.ID += 1
        
    def get_details(self):
        print("ID:", Student.ID)
        print("Name:", self.name)
        print("Department:", self.department)
        print("Age:",self.age)
        print("CGPA:", self.cgpa)
        
        
    @classmethod   
    def from_String(cls, details):
        details = details.split('-')
        obj = cls(details[0], details[1], details[2], details[3])
        return obj
        
    
        
    




s1 = Student("Samin", "CSE", 21, 3.91)
s1.get_details()
print("-----------------------")
s2 = Student("Fahim", "ECE", 21, 3.85)
s2.get_details()
print("-----------------------")
s3 = Student("Tahura", "EEE", 22, 3.01)
s3.get_details()
print("-----------------------")
s4 = Student.from_String("Sumaiya-BBA-23-3.96")
s4.get_details()
print("aas")


# In[15]:


# task 2
class Assassin:
    assignment = 0
    def __init__(self, name, rate):
        self.name = name
        self.rate = rate
        Assassin.assignment += 1
        
    def printDetails(self):
        print("Name:", self.name)
        print("Success rate:", self.rate,"%")
        print("Total number of Assassin:", Assassin.assignment)


        
    @classmethod   
    def failureRate(cls, n,r):
        obj = cls(n, 100 - r)
        return obj
        
    @classmethod   
    def failurePercentage(cls, n,d):
        d = d[0:2]
        obj = cls(n, 100 - int(d))
        return obj


john_wick = Assassin('John Wick', 100)
john_wick.printDetails()
print('================================')
nagisa = Assassin.failureRate("Nagisa", 20)
nagisa.printDetails()
print('================================')
akabane = Assassin.failurePercentage("Akabane", "10%")
akabane.printDetails()


# In[6]:


class Passenger:
    count = 0
    def __init__(self, name):
        self.name =name
        self.fare = 450
        Passenger.count += 1
        
    def set_bag_weight(self, w):
        self.w = w
        if 21 <= w >= 50:
            self.fare = 550
        elif w >= 20:
            self.fare = 500
            
        elif w >= 50:
            self.fare = 450
            
    def printDetail(self):
        print("Name:", self.name)
        print("Bus Fare:", self.fare)
    


print("Total Passenger:", Passenger.count)
p1 = Passenger("Jack")
p1.set_bag_weight(90)
p2 = Passenger("Carol")
p2.set_bag_weight(10)
p3 = Passenger("Mike")
p3.set_bag_weight(25)
print("=========================")
p1.printDetail()
print("=========================")
p2.printDetail()
print("=========================")
p3.printDetail()
print("=========================")
print("Total Passenger:", Passenger.count)


# In[8]:


class Passenger:
    count = 0
    
    def __init__(self, name):
        self.name =name
        self.fare = 450
        Passenger.count += 1
    
    @classmethod
    def weight_fun(cls, w):
        if w<=20:
            return 0
        elif w<=50:
            return 50
        else:
            return 100
        
    def set_bag_weight(self, w):
        self.w=w
        self.fare += Passenger.weight_fun(w)
        
    def printDetail(self):
        print("Name:", self.name)
        print("Bus Fare:", self.fare)
        

print("Total Passenger:", Passenger.count)
p1 = Passenger("Jack")
p1.set_bag_weight(90)
p2 = Passenger("Carol")
p2.set_bag_weight(10)
p3 = Passenger("Mike")
p3.set_bag_weight(25)
print("=========================")
p1.printDetail()
print("=========================")
p2.printDetail()
print("=========================")
p3.printDetail()
print("=========================")
print("Total Passenger:", Passenger.count)


# In[11]:


class Travel:
    count = 0
    def __init__(self, s, d):
        self.s = s
        self.d = d
        Travel.count += 1
        self.time = '1:00'
        
    def set_time(self, time):
        self.time = str(time) + ":00"
        
    def set_destination(self, d):
        self.d = d
        
    def set_source(self,s):
        self.s = s
        
    def display_travel_info(self):
        return "Source: {}\nDestination: {}\nFlight Time: {}".format(self.s,self.d,self.time)
        
    


print("No. of Traveller =", Travel.count)
print("=======================")
t1 = Travel("Dhaka","India")
print(t1.display_travel_info())
print("=======================")
t2 = Travel("Kuala Lampur","Dhaka")
t2.set_time(23)
print(t2.display_travel_info())
print("=======================")
t3 = Travel("Dhaka","New_Zealand")
t3.set_time(15)
t3.set_destination("Germany")
print(t3.display_travel_info())
print("=======================")
t4 = Travel("Dhaka","India")
t4.set_time(9)
t4.set_source("Malaysia")
t4.set_destination("Canada")
print(t4.display_travel_info())
print("=======================")
print("No. of Traveller =", Travel.count)


# In[15]:


class Employee:
    def __init__(self, name, workingPeriod):
        self.name = name
        self.workingPeriod = workingPeriod
        
    @classmethod
    def employeeByJoiningYear(cls, name, year):
        workingPeriod = 2022 - year
        return cls(name, workingPeriod)
    
    @staticmethod
    def experienceCheck(workingPeriod, gender):
        if workingPeriod < 3:
            if gender == "male":
                return "He is not experienced"
            else:
                return "She is not experienced"
            
        else:
            if gender == "male":
                return "He is experienced"
            else:
                return "She is experienced"
            
        
    


employee1 = Employee('Dororo', 3)
employee2 = Employee.employeeByJoiningYear('Harry', 2016)
print(employee1.workingPeriod)
print(employee2.workingPeriod)
print(employee1.name)
print(employee2.name)
print(Employee.experienceCheck(2, "male"))
print(Employee.experienceCheck(3, "female"))


# In[26]:


class Laptop:
    laptopCount = 0
    
    def __init__(self, name, count):
        self.name = name
        self.count = count
        Laptop.addcount(count)
        
    
    @classmethod
    def addcount(cls, count):
        cls.laptopCount += count
        


        
        
    @classmethod
    def advantage(cls):
        print("Laptops are portable")
        
    @classmethod
    def resetCount(cls):
        cls.laptopCount = 0
    def printCat(self):
        print("{} cat is {}".format(self.color, self.work)
        
        

        


lenovo = Laptop("Lenovo", 5);
dell = Laptop("Dell", 7);
print(lenovo.name, lenovo.count)
print(dell.name, dell.count)
print("Total number of Laptops", Laptop.laptopCount)
Laptop.advantage()
Laptop.resetCount()
print("Total number of Laptops", Laptop.laptopCount)


# In[25]:


class Cat:
    Number_of_cats = 0
    
    def __init__(self, color, work):
        self.color = color
        self.work = work
        Cat.Number_of_cats += 1
        
        


    
    @classmethod
    def  no_parameter(cls, color = "While", work = "sitting"):
        return cls(color, work)
    
    @classmethod
    def first_parameter(cls, color, work = "sitting"):
        return cls(color, work)
    @classmethod
    def second_parameter(cls, work):
        color = "Grey"
        return cls(color, work)
    
    def changeColor(self, color):
        self.color = color
    
    def printCat(self):
        print("{} cat is {}".format(self.color, self.work))
              

        


        
        

            

print("Total number of cats:", Cat.Number_of_cats)
c1 = Cat.no_parameter()
c2 = Cat.first_parameter("Black")
c3 = Cat("Brown", "jumping")
c4 = Cat("Red", "purring")
c5 = Cat.second_parameter("playing")
print("=======================")
c1.printCat()
c2.printCat()
c3.printCat()
c4.printCat()
c5.printCat()
c1.changeColor("Blue")
c3.changeColor("Purple")
c1.printCat()
c3.printCat()
print("=======================")
print("Total number of cats:", Cat.Number_of_cats)


# In[8]:





# In[24]:


class Cat:

    Number_of_cats = 0

    def __init__(self, c, a):
        self.c = c
        self.a = a

        Cat.Number_of_cats += 1


    @classmethod
    def no_parameter(cls,c = "White",a = "sitting"):
        
        
        return cls(c, a)

    @classmethod
    def first_parameter(cls, c,a = "sitting"):
        
        return cls(c, a)

    @classmethod
    def second_parameter(cls, a):
        c = "Grey"
        return cls(c, a)
    

    def changeColor(self, c):
        self.c = c
    

    def printCat(self):
        print ("{} cat is {}".format(self.c, self.a))
              



print("Total number of cats:", Cat.Number_of_cats)
c1 = Cat.no_parameter()
c2 = Cat.first_parameter("Black")
c3 = Cat("Brown", "jumping")
c4 = Cat("Red", "purring")
c5 = Cat.second_parameter("playing")
print("=======================")
c1.printCat()
c2.printCat()
c3.printCat()
c4.printCat()
c5.printCat()
c1.changeColor("Blue")
c3.changeColor("Purple")
c1.printCat()
c3.printCat()
print("=======================")
print("Total number of cats:", Cat.Number_of_cats)


# In[36]:


import math
class Cylinder:
    radius = 5
    height = 18
    
    def __init__(self, r =radius, h=height):
        self.radius = r
        self.height = h
        print("Default radius=",Cylinder.radius, "and height=",Cylinder.height)
        print("Updated: radius=", self.radius, "and height=",self.height)
        Cylinder.update_class_variable(r,h)
        
    
    @classmethod
    def swap(cls, h, r):
        return cls(r,h)
    
    @classmethod
    def changeFormat(cls,input):
        input = input.split('-')
        d = cls(float(input[0]),float(input[1]))
        return d
    
    
    @classmethod
    def update_class_variable(cls,r,h):
        cls.radius = r
        cls.height = h
        
    @staticmethod
    def area(r,h):
        total_area = 2 * math.pi * r *(r+h)
        print('Area: {}'.format(total_area))
    @staticmethod
    def volume(r,h):
        total_volume = math.pi * r * r * h
        print('Volume: {}'.format(total_volume))
        
        
    
    


c1 = Cylinder(0,0)
Cylinder.area(c1.radius,c1.height)
Cylinder.volume(c1.radius,c1.height)
print("===============================")
c2 = Cylinder.swap(8,3)
c2.area(c2.radius,c2.height)
c2.volume(c2.radius,c2.height)
print("===============================")
c3 = Cylinder.changeFormat("7-13")
c3.area(c3.radius,c3.height)
c3.volume(c3.radius,c3.height)
print("===============================")
Cylinder(0.3,5.56).area(Cylinder.radius,Cylinder.height)
print("===============================")
Cylinder(3,5).volume(Cylinder.radius,Cylinder.height)


# In[39]:


class Student:
  total_s = 0
  bracu_s = 0
  other_s = 0
  @classmethod
  def createStudent(cls,n,d,inst='BRAC University'):
    return cls(n,d,inst)
  @classmethod
  def printDetails(cls):
    print('Total Student(s): {}\nBRAC University Student(s): {}\nOther Institution Student(s): {}'.
          format(cls.total_s,cls.bracu_s,cls.other_s))
  @classmethod
  def updateCount(cls,inst):
    cls.total_s+=1
    if (inst=='BRAC University'):
      cls.bracu_s+=1
    else:
      cls.other_s+=1
    
  def __init__(self,n,d,inst='BRAC University'):
    self.n = n
    self.d = d
    self.inst = inst
    Student.updateCount(inst)
    
  def individualDetail(self):
    print('Name: {}\nDepartment: {}\nInstitution: {}'.format(self.n,self.d,self.inst))



Student.printDetails()
print('#########################')
mikasa = Student('Mikasa Ackerman', "CSE")
mikasa.individualDetail()
print('------------------------------------------')
Student.printDetails()
print('========================')
harry = Student.createStudent('Harry Potter', "Defence Against Dark Arts", "Hogwarts School")
harry.individualDetail()
print('-------------------------------------------')
Student.printDetails()
print('=========================')
levi = Student.createStudent("Levi Ackerman", "CSE")
levi.individualDetail()
print('--------------------------------------------')
Student.printDetails()


# In[40]:


class SultansDine:
  branchCount = 0
  sellCount = 0
  branches_info =[]
  @classmethod
  def details(cls):
    print('Total Number of branch(s): {}\nTotal Sell: {} Taka'.format(cls.branchCount,cls.sellCount))
    if (cls.branchCount>0):
      for item in cls.branches_info:
        print("Branch Name: {}, Branch Sell: {} Taka\nBranch consists of total sell's: {:.2f}% ".format(item[0],item[1],item[2]))

  @classmethod
  def update(cls,name,sell):
    cls.branchCount+=1
    cls.sellCount += sell
    sell_percentage = (sell/cls.sellCount)*100
    check = 0
    if ([name,sell,sell_percentage] not in cls.branches_info):
      cls.branches_info.append([name,sell,sell_percentage])

    for item in cls.branches_info:
      index = cls.branches_info.index(item)
      sell_percentage = (item[1]/cls.sellCount)*100
      cls.branches_info[index][2] = sell_percentage
      
  def __init__(self,name):
    self.b_name = name
    self.sell = 0

  def sellQuantity(self,quantity):
    if (quantity < 10):
      unit_price = 300
    elif (quantity < 20):
      unit_price = 350
    else:
      unit_price = 400
    self.sell += quantity * unit_price
    
    SultansDine.update( self.b_name , self.sell)

  def branchInformation(self):
    print('Branch Name: {}\nBranch Sell: {} Taka'.format(self.b_name,self.sell))

SultansDine.details()
print('########################')
dhanmodi = SultansDine('Dhanmondi')
dhanmodi.sellQuantity(25)
dhanmodi.branchInformation()
print('-----------------------------------------')
SultansDine.details()
print('========================')
baily_road = SultansDine('Baily Road')
baily_road.sellQuantity(15)
baily_road.branchInformation()
print('-----------------------------------------')
SultansDine.details()
print('========================')
gulshan = SultansDine('Gulshan')
gulshan.sellQuantity(9)
gulshan.branchInformation()
print('-----------------------------------------')
SultansDine.details()


# In[17]:


class A:
    temp = 4
    def __init__(self):
        self.y = self.temp - 2
        self.sum = self.temp + 1
        A.temp -= 2
        self.methodA(3, 4)
    def methodA(self, m, n):
        x = 0
        self.y = self.y + m + (self.temp)
        A.temp += 1
        x = x + 1 + n
        self.sum = self.sum + x + self.y
        print(x, self.y, self.sum)

class B:
    x = 0
    def __init__(self, b = None):
        self.y, self.temp, self.sum = 5, -5, 2
        if b == None:
            self.y = self.temp + 3
            self.sum = 3 + self.temp + 2
            self.temp -= 2
        else:
            self.sum = b.sum
            B.x = b.x
            b.methodB(2, 3)
    def methodA(self, m, n):
        x = 2
        self.y = self.y + m + (self.temp)
        self.temp += 1
        x = x + 5 + n
        self.sum = self.sum + x + self.y
        print(x, self.y, self.sum)
    def methodB(self, m, n):
        y = 0
        y = y + self.y
        B.x = self.y + 2 + self.temp
        self.methodA(self.x, y)
        self.sum = self.x + y + self.sum
        print(self.x, y, self.sum)

        
a1 = A()
b1 = B()
b2 = B(b1)
b1.methodA(1, 2)
b2.methodB(3, 2)


# In[12]:


class FinalT6A:
    temp = 3

    def __init__(self, x, p):
        self.sum, self.y = 0, 2
        FinalT6A.temp += 3
        self.y = self.temp - p
        self.sum = self.temp + x
        print(x, self.y, self.sum)

    def methodA(self):
        x, y = 0, 0
        y = y + self.y
        x = self.y + 2 + self.temp
        self.sum = x + y + self.methodB(self.temp, y)
        print(x, y, self.sum)

    def methodB(self, temp, n):
        x = 0
        FinalT6A.temp += 1
        self.y = self.y + (FinalT6A.temp)
        FinalT6A.temp -= 1
        x = x + 2 + n
        self.sum = self.sum + x + self.y
        print(x, self.y, self.sum)
        return self.sum
    
    
q1 = FinalT6A(2,1)
q1.methodA()
q1.methodA()


# In[7]:


class Puzzle:
    x = 0

    def methodA(self):
        Puzzle.x = 5
        z = Puzzle.x + self.methodB(Puzzle.x)
        print(Puzzle.x, z)
        z = self.methodB(z + 2) + Puzzle.x
        print(Puzzle.x, z)
        self.methodB(Puzzle.x, z)
        print(Puzzle.x, z)

    def methodB(self, *args):
        if len(args) == 1:
            y = args[0]
            Puzzle.x = y + Puzzle.x
            print(Puzzle.x, y)
            return Puzzle.x + 3
        else:
            z, x = args
            z = z + 1
            x = x + 1
            print(z, x)
            
p = Puzzle()
p.methodA()
p.methodA()
p = Puzzle()
p.methodA()
p.methodB(7)


# In[1]:


class msgClass:
    def __init__(self):
        self.content = 0
        

 
class Quiz3:
    x = 0
    def __init__(self, k = None):
        self.sum, self.y = 0, 0
        if k is None:
            self.sum = 5
            Quiz3.x = 2
            self.y = 2
        else:
            self.sum = self.sum + k
            self.y = 3
            Quiz3.x += 2 
            


    def methodA(self):
        x = 1
        y = 1
        msg = [None]
        myMsg = msgClass()
        
        myMsg.content = Quiz3.x
        
        msg[0] = myMsg
        

        msg[0].content = self.y + myMsg.content
        self.y = self.y + self.methodB(msg[0])
    

        y = self.methodB(msg[0]) + self.y


        x = y + self.methodB(msg, msg[0])
        

        self.sum = x + y + msg[0].content

        print(x, y, self.sum)

    def methodB(self, *args):

        if len(args) == 2:
            mg2, mg1 = args
            
            x = 2

            self.y = self.y + mg2[0].content

            mg2[0].content = self.y + mg1.content


            x = x + 2 + mg1.content

            self.sum = self.sum + x + self.y

            mg1.content = self.sum - mg2[0].content

            print(Quiz3.x, self.y, self.sum)

            return self.sum

        

        elif len(args) == 1:

            mg1, = args

            x = 1

            y = 2

            y = self.sum + mg1.content

            self.y = y + mg1.content

            x = Quiz3.x + 5 + mg1.content

            self.sum = self.sum + x + y

            Quiz3.x = mg1.content + x + 3

            print(x, y, self.sum)

            return y
        
        

a1 = Quiz3()
a2 = Quiz3(5)
msg = msgClass()
a1.methodA()
# a2.methodB(msg)
