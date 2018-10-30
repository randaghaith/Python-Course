#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n=int(input("Give a number To check the prime numbers: "))
def checkPrime(number):

    if number == 2 or number == 3 or number == 5:
        return True
    elif number % 2 == 0 or number % 3 == 0 or number % 5 == 0:
        return False
    else:
        for i in range(3,int(number**0.5)+1,2):   
            if number % i == 0:
                return False
                break
        else:
             return True

def prime_numbers(n):
    primeList = [] 
    count = 0
    prime = 2
    while count != n:
        if checkPrime(prime) == True:
            primeList.append(prime)
            count = count + 1
        prime = prime + 1
    return primeList

print(prime_numbers(n))

