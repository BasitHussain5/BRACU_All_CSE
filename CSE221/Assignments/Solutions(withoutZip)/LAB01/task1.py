#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Task 01a

with open("input1a.txt", "r") as file_in:
    x = file_in.readline()
    with open("output1a.txt", "w") as file_out:
        for i in range(int(x)):
            number = int(file_in.readline())
            if number % 2 == 0:
                file_out.write("{} is an Even Number.\n".format(number))
            else:
                file_out.write("{} is an Odd Number.\n".format(number))


# In[3]:


#Task 01b

with open("input1b.txt", "r") as file_in:
    y = file_in.readline()
    with open("output1b.txt", "w") as file_out:
        for i in range(int(y)):
            number = file_in.readline()
            lst = number.split(" ")
            ope = lst[2]
            if ope == "+":
                result = int(lst[1]) + int(lst[3])
            elif ope == "-":
                result = int(lst[1]) - int(lst[3])
            elif ope == "/":
                result = int(lst[1]) / int(lst[3])
            else:
                result = int(lst[1]) * int(lst[3])
    
            file_out.write("The result of {} {} {} is {}.\n". format(lst[1],lst[2],lst[3], result))


# In[ ]:




