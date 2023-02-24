#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Task 01

class calculator:
    def __init__(self):
        self.first_value =  int(input())
        self.operator = input()
        self.second_value = int(input())
        print("Let’s Calculate!")
        print("Value 1:", self.first_value)
        print("Operator:",self.operator )
        print("Value 2:",self.second_value )
    def add(self):
        if self.operator == "+":
            print("Result:",self.first_value +   self.second_value)
    def subtract(self):
        if self.operator == "-":
            print("Result:",self.first_value -   self.second_value)
    def multiply(self):
        if self.operator == "*":
            print("Result:",self.first_value *   self.second_value)
    def divide(self):
        if self.operator == "/":
            print("Result:",self.first_value /   self.second_value)
        
obj = calculator()
obj.add()
obj.subtract()
obj.multiply()
obj.divide()


# In[2]:


# Task 02:

class Customer:
    def __init__(self,name):
        self.name = name
        
    def greet(self, info = None):
        
        if info == None:
            print("Hello!")
        else:
            print("Hello",info+"!")
        
    def purchase(self,*purchase):
        print(self.name+",","you purchased",len(purchase),"items(s):")
        for i in purchase:
            print(i)
        

customer_1 = Customer("Sam")
customer_1.greet()
customer_1.purchase("chips", "chocolate", "orange juice")
print("-----------------------------")
customer_2 = Customer("David")
customer_2.greet("David")
customer_2.purchase("orange juice")


# In[3]:


# Task 03:

class Panda:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
        
    def sleep(self, info = None):
        if info == None:
            return ("{} duration is unknown thus should have only bamboo leaves".format(self.name))
        else:
            if 3 <= info <=5:
                return ("{} sleeps {} hours daily and should have Mixed Veggies".format(self.name,info))
            elif 6 <= info <= 8:
                return ("{} sleeps {} hours daily and should have Eggplant & Tofu".format(self.name,info))
            elif 9 <= info <= 11:
                return ("{} sleeps {} hours daily and should have Broccoli Chicken".format(self.name,info))
                

panda1 = Panda("Kunfu","Male", 5)
panda2=Panda("Pan Pan","Female",3)
panda3=Panda("Ming Ming","Female",8)
print("{} is a {} Panda Bear who is {} years old".format(panda1.name,panda1.gender,panda1.age))
print("{} is a {} Panda Bear who is {} years old".format(panda2.name,panda2.gender,panda2.age))
print("{} is a {} Panda Bear who is {} years old".format(panda3.name,panda3.gender,panda3.age))
print("===========================")
print(panda2.sleep(10))
print(panda1.sleep(4))
print(panda3.sleep())


# In[4]:


#Task 04
class Cat:
    def __init__(self, color = None, work = None):
        if color == None and work == None:
            self.color = "White"
            self.work = "sitting"
        elif color != None and work == None:
            self.color = color
            self.work = "sitting"
        else:
            self.color = color
            self.work = work
    def printCat(self):
        print("{} cat is {}".format(self.color, self.work))
    def changeColor(self, colorr):
        if self.color == "Black":
            self.color == colorr
        elif self.color == "Brown":
            self.color = colorr
        

c1 = Cat()
c2 = Cat("Black")
c3 = Cat("Brown", "jumping")
c4 = Cat("Red", "purring")
c1.printCat()
c2.printCat()
c3.printCat()
c4.printCat()
c1.changeColor("Blue")
c3.changeColor("Purple")
c1.printCat()
c3.printCat()


# In[5]:


# Task 05:

class Student:
    def __init__(self, name = None):
        if name == None:
            self.name = "default student"
        else:
            self.name = name
    def quizcalc(self, *score):
        self.ave = sum(score)/3
        
    def printdetail(self):
        print("Hello", self.name)
        print("Your average quiz score is",self.ave)
    
            
            


s1 = Student()
s1.quizcalc(10)
print('--------------------------------')
s1.printdetail()
s2 = Student('Harry')
s2.quizcalc(10,8)
print('--------------------------------')
s2.printdetail()
s3 = Student('Hermione')
s3.quizcalc(10,9,10)
print('--------------------------------')
s3.printdetail()


# In[5]:


# task 06:

class Vehicle:
    def __init__(self):
        self.a = [0,0]
        
    def moveUp(self):
        self.a[1] += 1
        
    def moveLeft(self):
        self.a[0] -= 1
        
    def moveDown(self):
        self.a[1] -= 1
        
    def moveRight(self):
        self.a[0] += 1
        
    def print_position(self):
        print(tuple(self.a))
        
    

car = Vehicle()
car.print_position()
car.moveUp()
car.print_position()
car.moveLeft()
car.print_position()
car.moveDown()
car.print_position()
car.moveRight()


# In[7]:


# Task 07:

class Programmer:
    def __init__(self, *info):
        self.name = info[0]
        self.lang = info[1]
        self.expe = info[2]
        print("Horray! A new programmer is born")
    def addExp(self, exp):
        self.expe += exp
        print("Updating experience of",self.name)
    def printDetails(self):
        print("Name: ", self.name)
        print("language: ", self.lang)
        print("Experience: ",self.expe,"years.")
        
        


p1 = Programmer("Ethen Hunt", "Java", 10)
p1.printDetails()
print('--------------------------')
p2 = Programmer("James Bond", "C++", 7)
p2.printDetails()
print('--------------------------')
p3 = Programmer("Jon Snow", "Python", 4)
p3.printDetails()
p3.addExp(5)
p3.printDetails()


# In[6]:


# Task 08:

class Student:
    def __init__(self, name, id, dep=None):
        if dep == None:
            self.name = name
            self.id = id
            self.dep = "CSE"
        else:
        
            self.name = name
            self.id = id
            self.dep = dep
    def dailyEffort(self, hour):
        self.hour = hour
    def printDetails(self):
        print("Name:",self.name)
        print("ID:", self.id)
        print("Department:", self.dep)
        print("Daily Effort:",self.hour,"hour(s)")
        if self.hour <= 2:
            self.hour = "Should give more effort!'"
        elif self.hour <= 4:
            self.hour = "Keep up the good work!'"
        else:
            self.hour = "Excellent! Now motivate others.'"
    
        print("Suggestion:",self.hour)
        
        

harry = Student('Harry Potter', 123)
harry.dailyEffort(3)
harry.printDetails()
print('========================')
john = Student("John Wick", 456, "BBA")
john.dailyEffort(2)
john.printDetails()
print('========================')
naruto = Student("Naruto Uzumaki", 777, "Ninja")
naruto.dailyEffort(6)
naruto.printDetails()


# In[9]:


# Task 09:

class Patient:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def add_Symptom(self, *symp):
        self.sym = ""
        for i in symp:
            if i == symp[-1]:
                self.sym += i
            else:
                self.sym += i + ", "
    def printPatientDetail(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Symptoms:", self.sym)
            

p1 = Patient("Thomas", 23)
p1.add_Symptom("Headache")
p2 = Patient("Carol", 20)
p2.add_Symptom("Vomiting", "Coughing")
p3 = Patient("Mike", 25)
p3.add_Symptom("Fever", "Headache", "Coughing")
print("=========================")
p1.printPatientDetail()
print("=========================")
p2.printPatientDetail()
print("=========================")
p3.printPatientDetail()
print("=========================")


# In[7]:


# Task 10:

class Avengers:
    def __init__(self, name, partner):
        self.name = name
        self.partner = partner
    def super_powers(self, *sup):
        self.super = ""
        for i in sup:
            if i == sup[-1]:
                self.super += i
            else:
                self.super += i + ", "
    def printAvengersDetail(self):
        print("Name:",self.name)
        print("Partner:",self.partner)
        print("Super powers:",self.super)
            

a1 = Avengers('Captain America', 'Bucky Barnes')
a1.super_powers('Stamina', 'Slowed ageing')
a2 = Avengers('Doctor Strange', 'Ancient One')
a2.super_powers('Mastery of magic')
a3 = Avengers('Iron Man', 'War Machine')
a3.super_powers('Genius level intellect', 'Scientist ')
print("=========================")
a1.printAvengersDetail()
print("=========================")
a2.printAvengersDetail()
print("=========================")
a3.printAvengersDetail()
print("=========================")


# In[26]:


# Task 11:

class Shinobi:
    def __init__(self, *info):
        self.name = info[0]
        self.rank = info[1]
        self.mission = 0
        
        

    def calSalary(self, missions):
            self.mission = missions
    def changeRank(self,changeR):
        self.rank = changeR


    def printInfo(self):
        print("Name:", self.name)
        print("Rank:", self.rank)
        print("Number of mission:", self.mission)
        if self.rank == "Genin":
            salary = self.mission * 50
        elif self.rank == "Chunin":
            salary = self.mission * 100
        else:
            salary = self.mission * 500
        print("Salary:", salary)
            
        


naruto = Shinobi("Naruto", "Genin")
naruto.calSalary(5)
naruto.printInfo()
print('====================')
shikamaru = Shinobi('Shikamaru', "Genin")
shikamaru.printInfo()
shikamaru.changeRank("Chunin")
shikamaru.calSalary(10)
shikamaru.printInfo()
print('====================')
neiji = Shinobi("Neiji", "Jonin")
neiji.calSalary(5)
neiji.printInfo()


# In[8]:


# Task 12:

class ParcelKoro:
    def __init__(self, cosName = None, product_weight = None):
        if cosName == None and product_weight == None:
            self.cosName = "No name set"
            self.product_weight = 0
        elif cosName != None and product_weight == None:
            self.cosName = cosName
            self.product_weight = 0
        else:
            self.cosName = cosName
            self.product_weight = product_weight
            
    def calculateFee(self, locfee=None):
        if locfee == None:
            self.locfee = 50
        else:
            self.locfee = 100
    def printDetails(self):
        print("Costomer Name:", self.cosName)
        print("Product Weight:",self.product_weight)
        if self.locfee == None:
            if self.product_weight != 0:
                fee = (self.product_weight * 20) + self.locfee            
                
            else:
                fee = (0)
        else:
            if self.product_weight != 0:
                fee = (self.product_weight * 20) + self.locfee
            else:
                fee = (0)
            print("Total fee:",fee)
                
            
        

print("**********************")
p1 = ParcelKoro()
p1.calculateFee()
p1.printDetails()
print("**********************")
p2 = ParcelKoro('Bob The Builder')
p2.calculateFee()
p2.printDetails()
print("----------------------------")
p2.product_weight = 15
p2.calculateFee()
p2.printDetails()
print("**********************")
p3 = ParcelKoro('Dora The Explorer', 10)
p3.calculateFee('Dhanmondi')
p3.printDetails()


# In[45]:


# Task 13:

class Batsman:
    def __init__(self, *info):
        if len(info) == 2:
            self.name = "new Batsman"
            self.score = info[-2]
            self.ballface = info[-1]
        else:
            self.name = info[0]
            self.score = info[-2]
            self.ballface = info[-1]           

    def setName(self,nam):
        self.name = nam
            
    def battingStrikeRate(self):
        return ((self.score/self.ballface) * 100)
    def printCareerStatistics(self):
        print("Name:", self.name)
        print("Runs Score:",self.score,", Balls Faced:",self.ballface)



b1 = Batsman(6101, 7380)
b1.printCareerStatistics()
print("============================")
b2 = Batsman("Liton Das", 678, 773)
b2.printCareerStatistics()
print("----------------------------")
print(b2.battingStrikeRate())
print("============================")
b1.setName("Shakib Al Hasan")
b1.printCareerStatistics()
print("----------------------------")
print(b1.battingStrikeRate())


# In[9]:


#task 14

class EPL_Team:
    def __init__(self, name, song = "No Slogan",title=0):
        self.name = name
        self.song = song
        self.title = title
            
    def increaseTitle(self):
        self.title = 1
        
    
    def changeSong(self,news):
        self.song = news
    def showClubInfo(self):
        return ("""Name: {}
Song: {}
Total No of title {}""".format(self.name, self.song, self.title))
            



manu = EPL_Team('Manchester United', 'Glory Glory Man United')
chelsea = EPL_Team('Chelsea')
print('===================')
print(manu.showClubInfo())
print('##################')
manu.increaseTitle()
print(manu.showClubInfo())
print('===================')
print(chelsea.showClubInfo())
chelsea.changeSong('Keep the blue flag flying high')
print(chelsea.showClubInfo())


# In[88]:


# Task 15:

class Account:
    def __init__(self, name = None, balance = None):
        if name == None and balance == None:
            self.name = "Default Account"
            self.balance = 0.0
        elif name != None and balance == None:
            self.name = name
            self.balance = 0.0
        else:
            self.name = name
            self.balance = balance
            
    def withdraw(self, m):
        if self.balance - m <= 3070.0:
            print("""Sorry, Withdraw unsuccessful! The account
balance after deducting withdraw amount is
equal to or less than minimum.""")
        else:
            print("Withdraw successful! New balance is:",self.balance - m)
    def details(self):
        return ("""{}
{}""".format(self.name,self.balance))
        
        
        
    


a1 = Account()
print(a1.details())
print("------------------------")
a1.name = "Oliver"
a1.balance = 10000.0
print(a1.details())
print("------------------------")
a2 = Account("Liam")
print(a2.details())
print("------------------------")
a3 = Account("Noah",400)
print(a3.details())
print("------------------------")
a1.withdraw(6930)
print("------------------------")
a2.withdraw(600)
print("------------------------")
a1.withdraw(6929)


# In[10]:


# Task 16:

#task 16
class Author:
    def __init__(self, name = None, *info):
        if name != None:
            self.name = name
            self.info = info
        else:
            self.name = "Default"
            self.info = info

    def changeName(self,nam):
        self.name = nam
    def addBooks(self, *inf):
        self.info = inf
    def printDetails(self):
        print("Author Name:",self.name)
        print("--------")
        print("List of Books:")
        for i in self.info:
            print(i)

auth1 = Author('Humayun Ahmed')
auth1.addBooks('Deyal', 'Megher Opor Bari')
auth1.printDetails()
print("===================")
auth2 = Author()
print(auth2.name)
auth2.changeName('Mario Puzo')
auth2.addBooks('The Godfather', 'Omerta', 'The Sicilian')
print("===================")
auth2.printDetails()
print("==================")
auth3 = Author('Paolo Coelho', 'The Alchemist', 'The Fifth Mountain')
auth3.printDetails()


# In[11]:


# Task 17:

class Student:
    def __init__(self, name = None, dep = None):
        if name == None and dep == None:
            print("Student name and department need to be set")
        elif name != None and dep == None:
            self.name = name
            print("department for", self.name, "needs to be set")
        else:
            self.name = name
            self.dep = dep
            print(self.name, "is from", self.dep, "Department")
            
    def update_name(self, updateN):
        self.name = updateN
    def update_department(self, updateD):
        self.dep = updateD
    def enroll(self, *courses):
        self.courses = courses
    def printDetail(self):
        print("Name:", self.name)
        print("Department", self.dep)
        print(self.name, "enrolled in", len(self.courses), "course(s):")
        self.cour = ""
        for i in self.courses:
            if i == self.courses[-1]:
                self.cour += i
            else:
                self.cour += i + ", "
        print(self.cour)

s1 = Student()
print("=========================")
s2 = Student("Carol")
print("=========================")
s3 = Student("Jon", "EEE")
print("=========================")
s1.update_name("Bob")
s1.update_department("CSE")
s2.update_department("BBA")
s1.enroll("CSE110", "MAT110", "ENG091")
s2.enroll("BUS101")
s3.enroll("MAT110", "PHY111")
print("###########################")
s1.printDetail()
print("=========================")
s2.printDetail()
print("=========================")
s3.printDetail()


# In[12]:


# Task 18:

class Student:
    def __init__(self, *info):
        self.name = info[0]
        self.id = info[1]
        self.dep = info[2]
    def advise(self, *inf):
        if len(inf) == 3:
            self.a = inf[0]
            self.b = inf[1]
            self.c = inf[2]
            print(self.name, "you have taken 9.0 credits.")
            print("List of courses:", self.a,",",self.b,",",self.c )
            print("Status: Ok")
            
        elif len(inf) == 2:
            self.a = inf[0]
            self.b = inf[1]
            print(self.name, "you have taken 6.0 credits.")
            print("List of courses:", self.a,",",self.b)
            print("Status: OYou have to take at least 1 more courses")
            
            
        if len(inf) == 5:
            self.a = inf[0]
            self.b = inf[1]
            self.c = inf[2]
            self.d = inf[3]
            self.e = inf[4]
            print(self.name, "you have taken 15 credits.")
            print("List of courses:", self.a,",",self.b,",",self.c, ",",self.d)
            print("Status: You have to drop at least 1 course.")
    def details(self):
        return ("""Name: {}
ID: {}
Department: {}""".format(self.name, self.id, self.dep))

s1 = Student("Alice","20103012","CSE")
s2 = Student("Bob", "18301254","EEE")
s3 = Student("Carol", "17101238","CSE")
print("##########################")
print(s1.details())
print("##########################")
print(s2.details())
print("##########################")
s1.advise("CSE110", "MAT110", "PHY111")
print("##########################")
s2.advise("BUS101", "MAT120")
print("##########################")
s3.advise("MAT110", "PHY111", "ENG102",
"CSE111", "CSE230")
