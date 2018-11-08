#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
response = requests.get("http://data.fixer.io/api/latest?access_key=54d2d1cc5b13cfb69bee9211e9b117fe").json()
initial_curr=input("choose your currency : ")
if initial_curr in response['rates'] :
    final_curr=input("choose the currency you want to convert to: ")
    if final_curr in response['rates']:
        amount=float(input(" how much you want to convert ? "))
        initial_curr_rate=float(response['rates'][initial_curr])
        final_curr_rate=float(response['rates'][final_curr])
        result=((final_curr_rate/initial_curr_rate)*amount)
    else:
        print("there is an error in your input")
        
else :
    print("there is an error in your input")
print(f"{ amount }{ initial_curr }to{ final_curr } is {result}")


# In[ ]:




