#!/usr/bin/env python
# coding: utf-8

# In[12]:


first=int(input("choose the number of currency you want to convert from (1.USD , 2.JOD , 3.TRL ) :"))
second=int(input("choose the number of currency you want to convert to (1.USD , 2.JOD , 3.TRL ): "))
x=float(input("Enter the mount you want to convert : "))
if first==1 and second==2 :
    print(f"the {x} USD = {x*.71} JOD ")
elif first==1 and second==3 :
    print(f"the {x} USD = {x*5.5} TRL ")
elif first==2 and second==1 :
    print(f"the {x} JOD = {x*1.41} USD ")
elif first==2 and second==3:
    print(f"the {x} JOD = {x*7.78} TRL ")
elif first==3 and second==1:
    print(f"the {x} TRL = {x*.18} USD ")
elif first==3 and second==2:
    print(f"the {x} TRL = {x*.13} JOD ")
else:
    print("Its same currency")

