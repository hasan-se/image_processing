#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os 
os.getcwd()
os.listdir()


# In[2]:


import numpy as np
import matplotlib.pyplot as plt


# In[5]:


im1=plt.imread('bird.jpg')
im1.shape
plt.imshow(im1)
plt.show()


# In[14]:



m,n,p = im1.shape
my_histogram={} #boş hash tablosu
for i in range(m):
     for j in range(n):
        s=(im1[i,j,0],im1[i,j,1],im1[i,j,2])
        if s in my_histogram_R_G_B.keys():
            my_histogram[s] = my_histogram[s] +1
        else:
            my_histogram[s] =1
            
my_histogram_R_G_B


# In[ ]:




