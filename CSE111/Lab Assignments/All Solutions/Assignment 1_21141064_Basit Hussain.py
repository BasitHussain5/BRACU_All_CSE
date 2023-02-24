#!/usr/bin/env python
# coding: utf-8

# In[4]:


#String task 01:

input_string = input()
upper_case_letters = 0
lower_case_letters = 0

for i in input_string:
    if ord(i) <= 122 and ord(i) >= 97:
        lower_case_letters += 1
    elif ord(i) <= 90 and ord(i) >= 65:
        upper_case_letters += 1


if upper_case_letters > lower_case_letters:
    print(input_string.upper())

else:
    print(input_string.lower())
        


# In[3]:


#String task 01: Another method

input_string = input("Enter a string:")

output = False
upper_case_letters = 0
lower_case_letters = 0

for i in input_string:
    if i.isupper():
        upper_case_letters += 1
    elif i.islower():
        lower_case_letters +=1
    else:
        output = True
        
if output == True:
    print("wrong input! Please type only letter.")

elif upper_case_letters > lower_case_letters:
    print(input_string.upper())

else:
    print(input_string.lower())


# In[6]:


#String Task 02:

input_string = input()

number_check = False
word_check = False
mixed_check = False

output = False

for i in input_string:
    if (ord(i) <= 90 and ord(i) >= 65) or (ord(i) <= 122 and ord(i) >=97):
        word_check = True
        
    elif ord(i) <= 57 and ord(i) >= 48:
        number_check = True
    else:
        mixed_check = True

if number_check == True and word_check == False and mixed_check == False:
    print("NUMBER")
    
elif number_check == False and word_check == True and mixed_check == False:
    print("WORD")
    
else: 
    print("MIXED")
    


# In[8]:


#string Task 02: Another Method

input_string = input("Enter a string:")

if input_string.isnumeric():
    print("NUMBER")
elif input_string.isalpha():
    print("WORD")
elif input_string.isnumeric() and input_string.isalpha():
    print("MIXED")
else:
    print("wrong input!")


# In[9]:


#String Task 03

input_data = input("Enter a string: ")
ind = ""
for i in input_data:
    if i.isupper():
        ind += str(input_data.index(i))
if int(ind[0])+1 != int(ind[1]):
    print(input_data[int(ind[0])+1:int(ind[1])])
else:
    print("BLANK")


# In[10]:


#String Task 03: Another Method

input_data = input("Enter a string: ")
ind = ""
for i in input_data:
    if ord(i) <= 90 and ord(i) >= 65:
        ind += str(input_data.index(i))
if int(ind[0])+1 != int(ind[1]):
    print(input_data[int(ind[0])+1:int(ind[1])])
else:
    print("BLANK")


# In[11]:


# String task 04:

input_data = input()
list_01 = []
if "too good" in input_data:
    list_01 = input_data.split("too good")
    new_string = list_01[0]+"excellent"+list_01[1]
    print(new_string)
else:
    print(input_data)


# In[12]:


# String task 04: Another method

input_data = input()

result = input_data.replace("too good", "excellent")

print(result)    


# In[13]:


# String task 04: Another method

input_data = input()

if "too good" in input_data:
    index = input_data.find("too good")
    new_string = input_data[0:index]+"excellent"+input_data[index+8:]
    print(new_string)
else:
    print(input_data)


# In[15]:


# Sting Task 05

input_data1, input_data2 = input().split(' ')

output = ""
for i in input_data1:
    if i in input_data2:
        output += i
        
for i in input_data2:
    if i in input_data1:
        output += i
        
if len(output) == 0:
    print("Nothing in common.")
else:
    print(output)


# In[18]:


# Sting Task 06

input_string = input("Enter a string:")
lowercase_letter = 0
uppercase_letter = 0
digit = 0
special_character = 0
output = ""

for i in input_string:
    if (ord(i) <= 90 and ord(i) >= 65):
        uppercase_letter += 1
        
    elif (ord(i) <= 122 and ord(i) >=97):
        lowercase_letter += 1
    elif (ord(i) <= 57 and ord(i) >=48):
        digit += 1
    elif ord(i) == 95 or ord(i) == 36 or ord(i) == 35 or ord(i) == 64:
        special_character += 1
        
        
if lowercase_letter == 0 and output == "":
    output += "Lowercase missing"
elif lowercase_letter == 0 and output != "":
    output += "Lowercase missing, "
if uppercase_letter == 0 and output == "":
    output += "Uppercase missing, "
elif uppercase_letter == 0 and output != "":
    output += "Uppercase missing"
if digit == 0 and output == "":
    output += "Digit missing "
elif digit ==0 and output != "":
    output += "Digit missing, "
if special_character == 0:
    output += "Special character missing"

if len(output) == 0:
    print("OK")
else:
    print(output)
        


# In[19]:


# List Task 01:

my_list = []
my_list_02 = []
while True:
    input_data = input()
    if input_data.lower() == "stop":
        break
    else:
        my_list.append(int(input_data))
for i in my_list:
    if i not in my_list_02:
        my_list_02.append(i)
        
for i in my_list_02:
    print(i,"-",my_list.count(i),"times")


# In[24]:


# List Task 01: By Using Dictionary

my_list = []
while True:
    input_data = input()
    if input_data.lower() == "stop":
        break
    else:
        my_list.append(int(input_data))
my_list

dic = {}
for element in my_list:
    if element in dic:
        dic[element] += 1
    else:
        dic[element] = 1

for values, keys in dic.items():
    print(values,"-",keys, "times")
        
        
    
        


# In[25]:


#### List Task 02:

num_of_test = int(input())

my_list = []
for i in range(num_of_test):
    input_data = list(map(int,input().strip().split()))
    my_list.append(input_data)

max_sum_list = max(my_list, key=sum)

list2 = []
for i in (my_list):
    list2.append(sum(i))
    
print(max(list2))
print(max_sum_list)


# In[26]:


# List Task 03:

my_list = []
for i in range(2):
    input_data = list(map(int,input().strip().split()))
    my_list.append(input_data)

sum_list = []
a = my_list[0]
b = my_list[1]
for j in range(len(a)):
    for i in range(len(b)):
        sum_list.append(a[j] * b[i])
print(sum_list)


# In[27]:


# List task 04:

while True:
    input_data = input()
    if input_data!='STOP':
        a = input_data.split(' ') 
        s_input_data =a
        input_data_list = []
        for i in s_input_data:
            input_data_list.append(int(i))
     
       
        b = []
        for i in range(len(input_data_list)-1):
            if (abs(input_data_list[i] - input_data_list[i+1])) in range(1, len(input_data_list)):
                b.append(input_data_list[i])
            else:
                break

        c = [(input_data_list[-1])]
        d = b+c

        if d == input_data_list:
            print("UB jumper")
        else:
            print("Not UB Jumper")
          
    else:
        break
    


# In[28]:


#### list Task 05:

input_string = input()
lowercase_letter = ""
uppercase_letter = ""
odd_digit = ""
even_digit = ""
for i in input_string:
    if (ord(i) <= 90 and ord(i) >= 65):
        uppercase_letter += i
        
    elif (ord(i) <= 122 and ord(i) >=97):
        lowercase_letter += i
    elif (ord(i) <= 57 and ord(i) >=48):
        if int(i) % 2 != 0:
            odd_digit += i
        else:
            even_digit += i

a = sorted(lowercase_letter)
b = sorted(uppercase_letter)
c = sorted(odd_digit)
d = sorted(even_digit)

output = ""

for i in a:
    output += i
for i in b:
    output += i
for i in c:
    output += i
for i in d:
    output += i
    
print(output)


# In[29]:


# List Task 06:

n, k = input().split(' ')



y = input()

y = list(y.split(" "))

list_1 = []

for i in range(int(n)):
    if (int(y[i])+int(k)) <= 5:
        list_1.append(int(y[i]))
        
output = len(list_1)//3

print(output)


# In[36]:


# Dictionary & Tuple Task 01:

input_data_01 = input()
list_1 = input_data_01.split(", ")

dictionary_01 = {}
for i in list_1:
    k, v = i.split(":")
    dictionary_01[k] = int(v)

    

input_data_02 = input()
list_2 = input_data_02.split(", ")

dictionary_02 = {}
for i in list_2:
    k, v = i.split(":")
    dictionary_02[k] = int(v)

    
for k, v in dictionary_02.items():
    if dictionary_01.get(k) == None:
        dictionary_01[k] = v
    else:
        dictionary_01[k] += v
        


lst = []
for v in dictionary_01.values():
    if v not in lst:
        lst.append(v)
lst.sort()


print(dictionary_01)
print("Values:",tuple(lst))
    
    

    


# In[37]:


# Dictionary & Tuple Task 02:

my_list = []
while True:
    input_data = input()
    if input_data == "STOP":
        break
    else:
        my_list.append(int(input_data))
my_list

dic = {}
for element in my_list:
    if element in dic:
        dic[element] += 1
    else:
        dic[element] = 1

for values, keys in dic.items():
    print(values,"-",keys, "times")


# In[43]:


# Dictionary & Tuple Task 03:

input_data_1 = input()
list_01 = input_data_1.split(", ")


dictionary_1 = {}

for i in list_01:
    k, v = i.split(":")
    dictionary_1[k] = v
    


list_02 = []

for k, v in dictionary_1.items():
    if k in dictionary_1:
        list_02.append((v,k))
        


dictionary_02 = {}
for i in list_02:
    k, v = i
    if k not in dictionary_02:
        dictionary_02[k] = []
        dictionary_02[k].append(v)
    else:
        dictionary_02[k].append(v)
        
print(dictionary_02)

    
        
        


# In[5]:







# In[44]:


# Dictionary & Tuple Task 04:

input_string_1 = input()
input_string_2 = input()

dic1 = {}

for i in input_string_1:
    if i in dic1:
        dic1[i] += 1
    else:
        dic1[i] = 1
        
dic2 = {}

for i in input_string_2:
    if i in dic2:
        dic2[i] += 1
    else:
        dic2[i] = 1
        
if (len(input_string_1) == len(input_string_2) and dic1 == dic2):
    print("Those strings are anagrams.")
else:
    print("Those strings are not anagrams.")
    
        
        
        


# In[48]:


# Dictionary & Tuple Task 05:

input_string = input()
cell_phones_text_keypad = {"1" : [".", ",", "?", "!", ":"],
                          "2" : ["A", "B", "C"],
                          "3" : ["D", "E", "F"],
                          "4" : ["G", "H", "I"],
                          "5" : ["J", "K", "L"],
                          "7" : ["P", "Q", "R", "S"],
                          "8" : ["T", "U", "V"],
                          "9" : ["W", "X", "Y", "Z"],
                          "0" : [" "]}

message_tex = input_string.upper()

output_message_in_number = ""

keys = list(cell_phones_text_keypad.items())

for i in range(len(message_tex)):
    for j in range(len(keys)):
        for k in range(len(keys[j][1])):
            if message_tex[i] == keys[j][1][k]:
                output_message_in_number += ((k+1) * keys[j][0])
                
print(int(output_message_in_number))
