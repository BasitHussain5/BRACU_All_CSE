#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Task 01
class RealNumber:
    def __init__(self, r=0):
        self.__realValue = r
    def getRealValue(self):
        return self.__realValue
    def setRealValue(self, r):
        self.__realValue = r
    def __str__(self):
        return 'RealPart: '+str(self.getRealValue())
    
class ComplexNumber(RealNumber):
    def __init__(self, r = 1, i = 1):
        super().__init__(float(r))
        self.i = float(i)
    def __str__(self):
        return super().__str__()+'\nImaginaryPart: ' + str(self.i)

cn1 = ComplexNumber()
print(cn1)
print('---------')
cn2 = ComplexNumber(5,7)
print(cn2)


# In[ ]:


#Task 2
class RealNumber:
    def __init__(self, number=0):
        self.number = number
    def __add__(self, anotherRealNumber):
        return self.number + anotherRealNumber.number
    def __sub__(self, anotherRealNumber):
        return self.number - anotherRealNumber.number
    def __str__(self):
        return str(self.number)

        

        
    
class ComexNumber(RealNumber):
    def __init__(self, r, i):
        self.i = i
        if type(r) == int:
            super().__init__(r)
        else:
            super().__init__(r.number)
            
    def __str__(self):
        if self.i < 0:
            return f"{str(self.number) + str(self.i)}i"
        else:
            return f"{self.number} + {self.i}i"
        
    def __add__(self, o):
        r_num = self.number + o.number
        i_num = self.number + o.number
        return ComplexNumber(r_num, i_num)
        
    def __sub__(self, o):
        r_num = self.number - o.number
        i_num = self.number - o.number
        return ComplexNumber(r_num, i_num)
            
    
    
r1 = RealNumber(3)
r2 = RealNumber(5)
print(r1+r2)
cn1 = ComplexNumber(2, 1)
print(cn1)
cn2 = ComplexNumber(r1, 5)
print(cn2)
cn3 = cn1 + cn2
print(cn3)
cn4 = cn1 - cn2
print(cn4)


# In[ ]:


#Task 03
class Account:
    def __init__(self, balance):
        self._balance = balance
    def getBalance(self):
        return self._balance
    
class CheckingAccount(Account):
    numberOfAccount = 0

    def __init__(self, balance=0.0):
        CheckingAccount.numberOfAccount += 1
        super().__init__(balance)
        
    def __str__(self):
        return f"Account Balance: {str(self.getBalance())}"
    
    
print('Number of Checking Accounts: ', CheckingAccount.numberOfAccount)
print(CheckingAccount())
print(CheckingAccount(100.00))
print(CheckingAccount(200.00))
print('Number of Checking Accounts: ', CheckingAccount.numberOfAccount)


# In[ ]:


#Task 04
class Fruit:
    def __init__(self, formalin=False, name=""):
        self.__formalin = formalin
        self.name = name

    def getName(self):
        return self.name

    def hasFormalin(self):
        return self.__formalin


class testFruit:
    def test(self, f):
        print("----Printing Detail----")
        if f.hasFormalin():
            print("Do not eat the", f.getName(), ".")
            print(f)
        else:
            print("Eat the", f.getName(), ".")
            print(f)


class Mango(Fruit, testFruit):
    def __init__(self, name="Mango", formalin=True):
        super().__init__(formalin, name)

    def __str__(self):
        if self.hasFormalin():
            return f"{self.getName()}s are bad for you"
        else:
            return f"{str(self.getName())}s are good for you"


class Jackfruit(Fruit, testFruit):
    def __init__(self, name="Jackfruit", formalin=False):
        super().__init__(formalin, name)

    def __str__(self):
        if self.hasFormalin():
            return f"{self.getName()}s are bad for you"
        else:
            return f"{str(self.getName())}s are good for you"
        


m = Mango()
j = Jackfruit()
t1 = testFruit()
t1.test(m)
t1.test(j)


# In[ ]:


#Task 05
class Exam:
    def __init__(self,marks):
        self.marks = marks
        self.time = 60
    def examSyllabus(self):
        return "Maths , English"
    def examParts(self):
        return "Part 1 - Maths\nPart 2 - English\n"
    
class ScienceExam(Exam):
    def __init__(self, marks, time, *parts):
        super().__init__(marks)
        self.time = time
        self.parts = parts
        
    def examSyllabus(self):
        a = super().examSyllabus()
        for i in self.parts:
            a += " , " + i
        return a
    
    def examParts(self):
        a = super().examParts()
        for i in range(len(self.parts)):
            a += 'Part {} - {}\n'.format(3+i,self.parts[i])
        return a[:-1]
    def __str__(self):
        return "Marks: {} Time: {} minutes Number of Parts: {}".format(self.marks,self.time,2+len(self.parts))
        

engineering = ScienceExam(100,90,"Physics","HigherMaths")
print(engineering)
print('----------------------------------')
print(engineering.examSyllabus())
print(engineering.examParts())
print('==================================')
architecture = ScienceExam(100,120,"Physics","HigherMaths","Drawing")
print(architecture)
print('----------------------------------')
print(architecture.examSyllabus())
print(architecture.examParts())


# In[ ]:


#Task 05
class Exam:
    def __init__(self,marks):
        self.marks = marks
        self.time = 60
    def examSyllabus(self):
        return "Maths , English"
    def examParts(self):
        return "Part 1 - Maths\nPart 2 - English\n"
    
class ScienceExam(Exam):
    def __init__(self, marks, time, *parts):
        super().__init__(marks)
        self.time = time
        self.parts = parts
        
    def examSyllabus(self):
        a = super().examSyllabus().split(",")
        for i in self.parts:
            a.append(i)
        for j in range(len(a)):
            return "Parts ", j+1,"-", a[j]
            
    
    def examParts(self):
        return len(a)
    def __str__(self):
        return "Marks: {} Time: {} minutes Number of Parts: {}".format(self.marks,self.time,(self.parts))
        

engineering = ScienceExam(100,90,"Physics","HigherMaths")
print(engineering)
print('----------------------------------')
print(engineering.examSyllabus())
print(engineering.examParts())
print('==================================')
architecture = ScienceExam(100,120,"Physics","HigherMaths","Drawing")
print(architecture)
print('----------------------------------')
print(architecture.examSyllabus())
print(architecture.examParts())


# In[ ]:


#Task 06
class Shape3D:
    pi = 3.14159
    def __init__(self, name = 'Default', radius = 0):
        self._area = 0
        self._name = name
        self._height = 'No need'
        self._radius = radius
    def calc_surface_area(self):
        return 2 * Shape3D.pi * self._radius
    def __str__(self):
        return "Radius: "+str(self._radius)
    
    
class Sphere(Shape3D):
    def __init__(self, name, radius):
        super().__init__(name, radius)
        print("Shape name: ", self._name, "Area Formula: 4 * pi * r * r")
        
    def calc_surface_area(self):
        self._area = super().calc_surface_area() * self._radius * 2
        
    def __str__(self):
        return "Radius: {}, Height: {}\nArea: {}".format(self._radius, self._height, self._area)
    
    
    
class Cylinder(Shape3D):
    def __init__(self, name, radius,height):
        super().__init__(name, radius)
        self._height = height
        print("Shape name: ", self._name, "Area Formula: 2 * pi * r * (r + h)"
        
    def calc_surface_area(self):
        self._area = super().calc_surface_area() * (self._radius + self._height)
        
    def __str__(self):
        return "Radius: {}, Height: {}\nArea: {}".format(self._radius, self._height, self._area)
    
    
    
    
    

sph = Sphere('Sphere', 5)
print('----------------------------------')
sph.calc_surface_area()
print(sph)
print('==================================')
cyl = Cylinder('Cylinder', 5, 10)
print('----------------------------------')
cyl.calc_surface_area()
print(cyl)


# In[5]:


#Task 06
class Shape3D:
    pi = 3.14159
    def __init__(self, name = 'Default', radius = 0):
        self._area = 0
        self._name = name
        self._height = 'No need'
        self._radius = radius
    def calc_surface_area(self):
        return 2 * Shape3D.pi * self._radius
    def __str__(self):
        return "Radius: "+str(self._radius)
    
    
class Sphere(Shape3D):
    def __init__(self, name, radius):
        super().__init__(name, radius)
        print("Shape name: ", self._name, "Area Formula: 4 * pi * r * r")
        
    def calc_surface_area(self):
        self._area = super().calc_surface_area() * self._radius * 2
        
    def __str__(self):
        return "Radius: {}, Height: {}\nArea: {}".format(self._radius, self._height, self._area)
    
    
    
class Cylinder(Shape3D):
    def __init__(self, name, radius,height):
        super().__init__(name, radius)
        self._height = height
        print("Shape name: ", self._name, "Area Formula: 2 * pi * r * (r + h)")
        
    def calc_surface_area(self):
        self._area = super().calc_surface_area() * (self._radius + self._height)
        
    def __str__(self):
        return "Radius: {}, Height: {}\nArea: {}".format(self._radius, self._height, self._area)
    
    
    
    
    

sph = Sphere('Sphere', 5)
print('----------------------------------')
sph.calc_surface_area()
print(sph)
print('==================================')
cyl = Cylinder('Cylinder', 5, 10)
print('----------------------------------')
cyl.calc_surface_area()
print(cyl)


# In[31]:


#Task 07

class PokemonBasic:
    def __init__(self, name = 'Default', hp = 0,
        weakness = 'None', type = 'Unknown'):
        self.name = name
        self.hit_point = hp
        self.weakness = weakness
        self.type = type
    def get_type(self):
        return 'Main type: ' + self.type
    def get_move(self):
        return 'Basic move: ' + 'Quick Attack'
    def __str__(self):
        return "Name: " + self.name + ", HP: " + str(self.hit_point) + ", Weakness: " + self.weakness
class PokemonExtra(PokemonBasic):
    def __init__(self, name, hp, weakness, type,sect = None,othc = None):
        super().__init__(name, hp, weakness, type)
        self.sect = sect
        self.othc = othc
    def get_type(self):
        if self.sect == None:
            return super().get_type()
        else:
            return super().get_type() + ", Secondary type: " + self.sect
    def get_move(self):
        if self.othc == None:
            return super().get_move()
        else:
                return super().get_move()+"\nOther move: " + str(self.othc[0]) + "," + str(self.othc[1])
                
        
print('\n------------Basic Info:--------------')
pk = PokemonBasic()
print(pk)
print(pk.get_type())
print(pk.get_move())
print('\n------------Pokemon 1 Info:-------------')
charmander = PokemonExtra('Charmander', 39, 'Water', 'Fire')
print(charmander)
print(charmander.get_type())
print(charmander.get_move())
print('\n------------Pokemon 2 Info:-------------')
charizard = PokemonExtra('Charizard', 78, 'Water', 'Fire', 'Flying', ('Fire Spin', 'Fire Blaze'))
print(charizard)
print(charizard.get_type())
print(charizard.get_move())


# In[11]:


#Task 08
class Team:
    def __init__(self, name):
        self.name = "default"
        self.total_player = 5
    def info(self):
        print("We love sports")
# Write your code here.

class FootBallTeam(Team):
    def __init__(self, name):
        self.name = name
        self.total_player = 11
    def info(self):
        print("Our name is ", self.name)
        print("we play FootBall")
        super().info()
        
class CricketTeam(Team):
    def __init__(self, name):
        self.name = name
        self.total_player = 11
    def info(self):
        print("Our name is ", self.name)
        print("we play Cricket")
        super().info()

class Team_test:
    def check(self, tm):
        print("=========================")
        print("Total Player: ", tm.total_player)
        tm.info()
        
        
f = FootBallTeam("Brazil")
c = CricketTeam("Bangladesh")
test = Team_test()
test.check(f)
test.check(c)


# In[35]:


#Task 09
class Pokemon:
    def __init__(self, p):
        self.pokemon = p
        self.pokemon_type = "Needs to be set"
        self.pokemon_weakness = "Needs to be set"
    def kind(self):
        return self.pokemon_type
    def weakness(self):
        return self.pokemon_weakness
    def what_am_i(self):
        print("I am a Pokemon.")
        
class Pikachu(Pokemon):
    def __init__(self, p = "Pikachu"):
        super().__init__(p)
        self.pokemon_type = "Electric"
        self.pokemon_weakness = "Ground"
        
    def what_am_i(self):
        super().what_am_i()
        print("I am Pikachu.")
        
class Charmander(Pokemon):
    def __init__(self, p = "Charmander"):
        super().__init__(p)
        self.pokemon_type = "Fire"
        self.pokemon_weakness = "water, Ground and Rock"
        
    def what_am_i(self):
        super().what_am_i()
        print("I am Charmander.")
        
        
        
        
pk1 = Pikachu()
print("Pokemon:", pk1.pokemon)
print("Type:", pk1.kind())
print("Weakness:", pk1.weakness())
pk1.what_am_i()
print("========================")
c1 = Charmander()
print("Pokemon:", c1.pokemon)
print("Type:", c1.kind())
print("Weakness:", c1.weakness())
c1.what_am_i()


# In[37]:


#Task 10

class Department:
    def __init__(self, s):
        self.semester = s
        self.name = "Default"
        self.id = -1
    def student_info(self):
        print("Name:", self.name)
        print("ID:", self.id)
    def courses(self, c1, c2, c3):
        print("No courses Approved yet!")
        
class CSE(Department):
    def __init__(self, n, id, semester):
        super().__init__(semester)
        self.name = n
        self.id = id
        self.dpt = "CSE"
        
    def courses(self, c1, c2, c3):
        print("Courses Approved to this", self.dpt, "student in", self.semester, "semeter :")
        print(c1+"\n"+c2+"\n"+c3)
        
        
class EEE(Department):
    def __init__(self, n, id, semester):
        super().__init__(semester)
        self.name = n
        self.id = id
        self.dpt = "EEE"
        
    def courses(self, c1, c2, c3):
        print("Courses Approved to this", self.dpt, "student in", self.semester, "semester :")
        print(c1+"\n"+c2+"\n"+c3)
        


        
        
        

s1 = CSE("Rahim", 16101328,"Spring2016")
s1.student_info()
s1.courses("CSE110", "MAT110", "ENG101")
print("==================")
s2 = EEE("Tanzim", 18101326, "Spring2018")
s2.student_info()
s2.courses("Mat110", "PHY111", "ENG101")
print("==================")
s3 = CSE("Rudana", 18101326, "Fall2017")
s3.student_info()
s3.courses("CSE111", "PHY101", "MAT120")
print("==================")
s4 = EEE("Zainab", 19201623, "Summer2019")
s4.student_info()
s4.courses("EEE201", "PHY112", "MAT120")
