#!/usr/bin/env python
# coding: utf-8

# In[ ]:


x=float(input("enter your number : "))
if x<-100:
    print(x*-1)
elif x>=-100 and x<=-25:
        print(x**4)
elif x>-25 and x<=0:
        print(3*(x**2)-1)
elif x>0 and x<=100:
        print((3.14/2)*2+3**x)
else:
        print(x)

