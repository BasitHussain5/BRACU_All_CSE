#!/usr/bin/env python
# coding: utf-8

# In[2]:


inp = open("input5.txt", "r")
outp = open("outpu5.txt", "w")
a = inp.readline()
l = []
for i in range(int(a)):
    l+=[inp.readline().split()]
b = sorted(l)

for i in range(int(a)):
        for j in range(int(a)):
            if b[i][0] == b[j][0]:
                if b[i][-1] > b[j][-1]:
                    b[i], b[j] = b[j], b[i]
for i in range(int(a)):
    outp.write(" ".join(b[i])+"\n")


# In[ ]:




