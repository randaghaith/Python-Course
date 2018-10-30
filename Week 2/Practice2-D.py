#!/usr/bin/env python
# coding: utf-8

# In[6]:


jordanStates = ["Irbid","Ajloun","Jerash","Mafraq","Balqa","Amman",
                "Zarqa","Madaba","Karak","Tafilah","Ma'an","Aqaba"]


for state in jordanStates:
    if state[0] == "A":
        print(state)

for state in jordanStates:
    if len(state) == 5:
        print(state)

