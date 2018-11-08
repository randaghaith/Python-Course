#!/usr/bin/env python
# coding: utf-8

# In[21]:


import requests

#'http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}'

LINK='http://api.openweathermap.org/data/2.5/forecast'

lat=float(input("input the city latitude you want :"))
lon=float(input("input the city longtidue you want :"))
add={
    
    "APPID":"247e66d2d5896cdbd53081720b12adcb",
    "lat":lat,
    "lon":lon
}

data=requests.get(LINK,add).json()
print(data)

