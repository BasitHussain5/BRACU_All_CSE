#!/usr/bin/env python
# coding: utf-8

# In[3]:





# Task 01:

def my_function(digit1, digit2):
    if digit2 != 0:
        if digit1 / digit2 not in range(0, 2):
            return ((digit1 / digit2) - int(digit1 / digit2))
        else:
            return (digit1 / digit2)
    else:
        return 0
    
input_1, input_2 = (input().split(', '))
inp1 = int(input_1)
inp2 = int(input_2)

my_function(inp1, inp2)


# In[4]:


# Task 01 Another Metrhod:

def my_function(input_1, input_2):
    try:
        if input_1 / input_2 not in range(0,2):
            return (input_1 / input_2) - int(input_1 / input_2)
        else:
            return (input_1 / input_2)
    except ZeroDivisionError:
        return 0

inp1 = 5 
inp2 = 2

my_function(inp1, inp2)
    


# In[8]:


# Tast 02:

def bmi_function(weight, hight):
    hight_convert_into_metter = 0.01 * hight
    bmi_farmula = weight / (hight_convert_into_metter)**2
    bmi = round(bmi_farmula, 1)
       
    if bmi < 18.5:
        print("Score is", str(bmi)+".","You are Underweight")
    elif 18.5 < bmi < 24.0:
        print("Score is", str(bmi)+".","Normal")
    elif 25 < bmi < 30:
        print("Score is", str(bmi)+".","You are Overweight")
    else:
        print("Score is", str(bmi)+".", "You are Obese")
        
input_1, input_2 = (input().split(', '))
inp1 = int(input_1)
inp2 = int(input_2)

bmi_function(inp2, inp1)

    
    


# In[10]:


# Task 03;

def my_function(minimum, maximum, divisor):
    result = 0
    for i in range(minimum, maximum):
        if i % divisor == 0:
            result += i
    return result
input_1, input_2, input_3 = (input().split(', '))
inp1 = int(input_1)
inp2 = int(input_2)
inp3 = int(input_3)

my_function(inp1, inp2, inp3)


# In[65]:


# Task 03 Another Method
def myfun(*inp):
    result = 0
    for i in range(inp[0], inp[1]):
        if i % inp[2] == 0:
            result += i
    return result

input_1, input_2, input_3 = (input().split(', '))
inp1 = int(input_1)
inp2 = int(input_2)
inp3 = int(input_3)

my_function(inp1, inp2, inp3)


# In[11]:


# task 04:
def function(bar, place = 'Mohakhali'):
    BBQ_Chicken_Cheese_Burger = 250
    Beef_Burger = 170
    Naga_Drums = 200
    tax = 0.08
    price = 0
    if bar == 'BBQ Chicken Cheese Burger':
        if place == 'Mohakhali':
            prince += BBQ_Chicken_Cheese_Burger + 40 + BBQ_Chicken_Cheese_Burger * tax
        else:
            prince += BBQ_Chicken_Cheese_Burger + 60 + BBQ_Chicken_Cheese_Burger * tax
            
    elif bar == 'Beef Burger':
        if place == 'Mohakhali':
            price += Beef_Burger + 40 + Beef_Burger * tax
        else:
            price += Beef_Burger + 60 + Beef_Burger * tax
            
            
    elif bar == 'Naga Drums':
        if place == 'Mohakhali':
            price += Naga_Drums + 40 + Naga_Drums * tax
        else:
            prince += Naga_Drums + 60 + Naga_Drums * tax
    else:
        print("Wrong input")
    return price
        
function('Beef Burger')


# In[12]:


# Task 05:
# Task 5

def replace_domain(email, newD, oldD = 'kaaj.com'):
    lst = email.split('@')
    
    if lst[1] == newD:
        print("Unchanged:",email)
    else:
        print("Changed:",lst[0]+"@"+newD)
 
    
    
replace_domain('alice@kaaj.com', 'sheba.xyz', 'kaaj.com')


# In[1]:


# Task 06:

def vowel_count_function(name):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    found_vowels = ''
    for i in name:
        if i in vowels:
            found_vowels += i+","
    if len(found_vowels) != 0:
        print("Vowels:", found_vowels, "Total number of vowels:", len(found_vowels))
    else:
        print("No vowels in the name")

vowel_count_function("Steve Jobs")            


# In[24]:


# Task 06:

def vowel_count_function(name):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    found_vowels = ''
    v = ""
    for i in name:
        if i in vowels:
            found_vowels += i
    if len(found_vowels) != 0:
        for i in range(len(found_vowels)):
            if found_vowels[i] == found_vowels[-1]:
                v += found_vowels[i]+"."
            else:
                v += found_vowels[i]+","
        print("Vowels:", v, "Total number of vowels:", len(found_vowels))
    else:
        print("No vowels in the name")

vowel_count_function("Steve jobs")            


# In[25]:


# Task 07:

def palindrome(name):
    reverse = name[::-1]
    if name == reverse:
        print("Palindrome")
    else:
        print("Not a palindrome")

palindrome('madama')
    


# In[27]:


# Task 8:

def funtion(days):
    years = days // 365
    mounth = (days % 365) // 30
    days = (days % 365) % 30
    print(years, "years,", mounth, "months and", days, "days")
inp = int(input())
funtion(inp)


# In[53]:


# Task 09:

def paragraph_checker_function(paragraph):
    lst_01 = list(paragraph.split(" "))
    lst_02 = [-1]
    copy_paragraph = ""
    for i in range(0, len(lst_01) - 1):
        if lst_01[i].endswith(".") or lst_01[i].endswith("!") or lst_01[i].endswith("?"):
            lst_02.append(i)
        elif lst_01[i] == "i":
            lst_01[i] = "I"
        for i in lst_02:
            x = lst_01[i + 1].capitalize()
            lst_01[i + 1] = x
    for i in lst_01:
        copy_paragraph += i + " "
    print(copy_paragraph)
inp = '''my favourite animal is a dog. a dog has sharp teeth so that it can eat flesh very easily. do you know my pet dog’s name? i love my pet very much.'''
paragraph_checker_function(inp)


# In[ ]:
