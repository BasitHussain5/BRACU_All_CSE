#!/usr/bin/env python
# coding: utf-8

# In[7]:


file_input = open("input4.txt", "r")
file_output = open("outpu4.txt", "w")

n = int(file_input.readline()[0])
ide = file_input.readline().split()
array = file_input.readline().split()

for i in range(n):
    for j in range(0, n-i-1):
        if array[j] < array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]
            ide[j], ide[j+1] = ide[j+1], ide[j]
        elif array[j] == array[j+1]:
            if ide[j] > ide[j+1]:
                ide[j], ide[j+1] = ide[j+1], ide[j]
for i in range(n):
    file_output.write("ID: {} Marks: {}\n".format(ide[i], array[i]))


# In[ ]:




