#!/usr/bin/env python
# coding: utf-8

# In[1]:


#task1 


# In[2]:


print('Hello World !')


# # weird numbers
# 
# import math
# import os
# import random
# import re
# import sys
# 
# 
# 
# if __name__ == '__main__':
#     n = int(input().strip())
# if n%2!=0:
#     print('Weird')
# else :
#     if n>=2 and n<=5:
#         print('Not Weird')
#     elif n>=6 and n<=20:
#         print('Weird')
#     else:
#         print('Not Weird')
# 

# 
#  if __name__ == '__main__':
#     a = int(input())
#     b = int(input())
#     print(a+b)
#     print(a-b)
#     print(a*b)
#     

# In[ ]:


# division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(int(a/b))
    print(a/b)


# In[ ]:


# leap year
def isleap(year):
   
    
    # Write your logic here
   if year % 4==0:
        return  True
   if year % 100==0:
        return True
   if year % 400==0:
        return True
   return False
        
 

year = int(input())
print(isleap(year))


# In[9]:


if __name__ == '__main__':
    n = int(input())
for i in range(0,n):
    print(i*i)


# In[13]:


if __name__ == '__main__':
    n = int(input())
for i in range(1,n+1):
    print(i,end="")


# In[ ]:




