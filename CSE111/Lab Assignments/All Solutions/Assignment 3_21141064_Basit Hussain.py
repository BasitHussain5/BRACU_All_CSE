#!/usr/bin/env python
# coding: utf-8

# In[28]:


# Task 01:
class DataType:
    def __init__(self, name, value):
        self.name = name
        self.value = value
data_type1 = DataType('Integer', 1234)
print(data_type1.name)
print(data_type1.value)
print('=====================')
data_type2 = DataType('String', 'Hello')
print(data_type2.name)
print(data_type2.value)
print('=====================')
data_type3 = DataType('Float', 4.0)
print(data_type3.name)
print(data_type3.value)


# In[29]:


# Task 02:
class Flower:
    def __init__(self):
        self.name = "Rose"
        self.color = "Red"
        self.num_of_petal = 6
flower1 = Flower()
flower1.name="Rose"
flower1.color="Red"
flower1.num_of_petal=6
print("Name of this flower:", flower1.name)
print("Color of this flower:",flower1.color)
print("Number of petal:",flower1.num_of_petal)
print("=====================")
flower2 = Flower()
flower2.name="Orchid"
flower2.color="Purple"
flower2.num_of_petal=4
print("Name of this flower:",flower2.name)
print("Color of this flower:",flower2.color)
print ("Number of petal:",flower2. num_of_petal)



print("Address of flower1: ",flower1)
print("Address of flower2: ",flower2)
print("They are same")


# In[8]:


#task 03:
class Wadiya():
    def __init__(self):
        self.name = 'Aladeen'
        self.designation = 'President Prime Minister Admiral General'
        self.num_of_wife = 100
        self.dictator = True
        
        
Wadiya = Wadiya()
print("Part 1:")
print("Name of President:",Wadiya.name)
print("Designation:",Wadiya.designation)
print("Number of wife:",Wadiya.num_of_wife)
print("Is he/she a dictator:",Wadiya.dictator)
print('=====================')

Wadiya.name = "Donald Trump"
Wadiya.designation = "President"
Wadiya.num_of_wife = 1
Wadiya.dictator = False

print("Part 2:")
print("Name of President:",Wadiya.name)
print("Designation:",Wadiya.designation)
print("Number of wife:",Wadiya.num_of_wife)
print("Is he/she a dictator:",Wadiya.dictator)

print("""
Answer. 04: Yes previous information is lost.""")


# In[30]:


class Joker:
    def __init__(self, name, power, is_he_psycho):
        self.name = name
        self.power = power
        self.is_he_psycho = is_he_psycho

j1 = Joker('Heath Ledger', 'Mind Game', False)
print(j1.name)
print(j1.power)
print(j1.is_he_psycho)
print("=====================")

j2 = Joker('Joaquin Phoenix', 'Laughing out Loud', True)
print(j2.name)
print(j2.power)
print(j2.is_he_psycho)
print("=====================")

if j1 == j2:
    print('same')
else:
    print('different')
j2.name = 'Heath Ledger'
if j1.name == j2.name:
    print('same')
else:
    print('different')
    
    
    
print("""Subtask:
2) The first if/else block prints the output as ‘different’, but why? Explain your answerand print your explanation at the very end.
Answer: Because the address / reference of objects j1 and j2 are differnt.""")
      
print("Address of j1 is", j1, 
      "and address of j2 is", j2,) 

print("""
updating the value of j2
3) The second if/else block prints the output as ‘same’, but why? Explain your answerand print your explanation at the very end.
Answer: Because we update the name of the object j2 (j2.name = 'Heath Ledger')""")


# In[31]:


# Task 05:
class Pokemon:
    def __init__(self, pokemon1_name, pokemon2_name, pokemon1_power, pokemon2_power,damage_rate):
        self.pokemon1_name = pokemon1_name
        self.pokemon2_name = pokemon2_name
        self.pokemon1_power = pokemon1_power
        self.pokemon2_power = pokemon2_power
        self.damage_rate = damage_rate
        


team_pika = Pokemon('pikachu', 'charmander', 90, 60, 10)
print('=======Team 1=======')
print('Pokemon 1:',team_pika.pokemon1_name,
team_pika.pokemon1_power)
print('Pokemon 2:',team_pika.pokemon2_name,
team_pika.pokemon2_power)
pika_combined_power = (team_pika.pokemon1_power +
team_pika.pokemon2_power) * team_pika.damage_rate
print('Combined Power:', pika_combined_power)


team_bulb = Pokemon('bulbasaur', 'squirtle', 80, 70, 9)
print('=======Team 2=======')
print('Pokemon 1:',team_bulb.pokemon1_name,
team_bulb.pokemon1_power)
print('Pokemon 2:',team_bulb.pokemon2_name,
team_bulb.pokemon2_power)
pika_combined_power = (team_bulb.pokemon1_power +
team_bulb.pokemon2_power) * team_bulb.damage_rate
print('Combined Power:', pika_combined_power)


# In[32]:


# Task 06:
class Player:
    def __init__(self):
        self.name = "Ronaldo"
        self.jersy_number = 9
        self.position = "Striker"

player1 = Player()
player1.name = "Ronaldo"
player1.jersy_number = 9
player1.position = "Striker"
print("Name of the Player:", player1.name)
print("Jersey Number of player:", player1.jersy_number)
print("Position of player:", player1.position)
print("===========================")
player2 = Player()
player2.name = "Neuer"
player2.jersy_number = 1
player2.position = "Goal Keeper"
print("Name of the player:", player2.name)
print("Jersey Number of player:", player2.jersy_number)
print("Position of player:", player2.position)


# In[33]:


#task 07:

class Country:
    def __init__(self):
        self.name = "Bangladesh"
        self.continent = "Asia"
        self.capital = "Dhaka"
        self.fifa_ranking = 187

country = Country()
print('Name:',country.name)
print('Continent:',country.continent)
print('Capital:',country.capital)
print('Fifa Ranking:',country.fifa_ranking)
print('===================')
country.name = "Belgium"
country.continent = "Europe"
country.capital = "Brussels"
country.fifa_ranking = 1
print('Name:',country.name)
print('Continent:',country.continent)
print('Capital:',country.capital)
print('Fifa Ranking:',country.fifa_ranking)


# In[34]:


#Task 08:
class DemonSlayer:
    def __init__(self, name, style, number_of_technique, kill):
        self.name = name
        self.style = style
        self.number_of_technique = number_of_technique
        self.kill = kill


tanjiro = DemonSlayer("Tanjiro", "Water Breathing", 10, 10)
print('Name:',tanjiro.name)
print('Fighting Style:',tanjiro.style)
print(f'Knows {tanjiro.number_of_technique} technique(s) and has killed {tanjiro.kill} demon(s)')
print('===================')
zenitsu = DemonSlayer("Zenitsu", "Thunder Breathing", 1, 4)
print('Name:',zenitsu.name)
print('Fighting Style:',zenitsu.style)
print(f'Knows {zenitsu.number_of_technique} technique(s) and has killed {zenitsu.kill} demon(s)')
print('===================')
inosuke = DemonSlayer("Inosuke", "Beast Breathing", 5, 7)
print('Name:',inosuke.name)
print('Fighting Style:',inosuke.style)
print(f'Knows {inosuke.number_of_technique} technique(s) and has killed {inosuke.kill} demon(s)')
print('===================')
print(f'{tanjiro.name}, {zenitsu.name}, {inosuke.name} knows total {tanjiro.number_of_technique + zenitsu.number_of_technique + inosuke.number_of_technique} techniques')
print(f'They have killed total {tanjiro.kill + zenitsu.kill + inosuke.kill} demons')


# In[35]:


# Task 09:

class box:
    def __init__(self, group):
        self.height = group[0]
        self.width = group[1]
        self.breadth = group[2]
        
        print("Creating a Box!")
        print("Volume of the box is", self.height*self.width*self.breadth, "cubic units.")

print("Box 1")
b1 = box([10,10,10])
print("=========================")
print("Height:", b1.height)
print("Width:", b1.width)
print("Breadth:", b1.breadth)
print("-------------------------")
print("Box 2")
b2 = box((30,10,10))
print("=========================")
print("Height:", b2.height)
print("Width:", b2.width)
print("Breadth:", b2.breadth)
b2.height = 300
print("Updating Box 2!")
print("Height:", b2.height)
print("Width:", b2.width)
print("Breadth:", b2.breadth)
print("-------------------------")
print("Box 3")
b3 = b2
print("Height:", b3.height)
print("Width:", b3.width)
print("Breadth:", b3.breadth)


# In[36]:


#Task 10
class buttons:
    def __init__(self, word, spaces, border):
        self.word = word
        self.spaces = spaces
        self.border = border
        print(self.word,"Button Specifications:")
        print("Button name:", word)
        print("Number of the border characters for the top and the bottom:", 1 + spaces + len(word) + spaces+ 1)
        print("""Number of spaces between the left side border and the first character of the button
name:""",spaces)
        print("""Number of spaces between the right side border and the last character of the button
name:""", spaces)
        print("Characters representing the borders:", border)
        print()
        print(border * (1 + spaces + len(word) + spaces+ 1))
        print(border+" "*spaces+word+" " *spaces+border)
        print(border * (1 + spaces + len(word) + spaces+ 1))
        
word = "CANCEL"
spaces = 10
border = 'x'
b1 = buttons(word, spaces, border)
print("=======================================================")
b2 = buttons("Notify",3, '!')
print("=======================================================")
b3 = buttons('SAVE PROGRESS', 5, '$')
