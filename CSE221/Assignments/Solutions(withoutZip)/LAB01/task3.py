#!/usr/bin/env python
# coding: utf-8

# In[ ]:


file_input = open("input3.txt", "r")
file_output = open("output3.txt", "w")
array = file_input.read().split()

def bubbleSort(array):
    m = int(array[0])
    for i in range(m):
        swp = False
        for j in range(1, m-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swp = True
        if swp == False:
            break

#######################

bubbleSort(array)
for i in range(1, len(array)):
    file_output.write(str(array[i]))
    file_output.write(" ")


# In[ ]:


# Here in this scenerio, if the given array will already being sorted then it will be the best case scenerio.
# we don not have to sort the array again in that case. that's why, the time complexity for the best case scenerio 
# is big Theta(n) 

