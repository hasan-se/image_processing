#!/usr/bin/env python
# coding: utf-8

# In[29]:


import matplotlib.pyplot as plt
import numpy as np


# In[30]:


def my_f_2(image_1 = plt.imread('istanbul_goruntu_isleme.jpg')):
    #image_1.ndim,image_1.shape
    m,n,p = image_1.shape
    my_histogram={} #boş hash tablosu
    for i in range(m):
        for j in range(n):
            if image_1[i,j,0] in my_histogram.keys():
                my_histogram[image_1[i,j,0]] = my_histogram[image_1[i,j,0]] +1
            else:
                my_histogram[image_1[i,j,0]] =1
    return my_histogram


# In[31]:


def my_f_3(my_histogram=my_f_2()):
    x=[]
    y=[]
    for key in my_histogram.keys():
        x.append(key)
        y.append(my_histogram[key])
    return x,y


# In[32]:


x,y=my_f_3()
plt.bar(x,y)
plt.show()


# In[ ]:




