#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

mylist = [23,76,97,28,10,8,2,4,6]

np_numbers = np.array(mylist)

print(np.mean(np_numbers))
print(np.median(np_numbers))
print(np.std(np_numbers))

