#!/usr/bin/env python
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt
import numpy as np


# In[14]:


im_1=plt.imread('maskfilter.jpg')


# In[28]:


im_2=np.zeros((250,303),dtype=np.uint8)
im_2=im_1[:,:,0]
im_3=im_1[:,:,0]
plt.imshow(im_2,cmap='gray')
plt.show


# In[29]:


im_2=im_1[:,:,0]
im_3=im_1[:,:,0]


# In[30]:


im_3=np.zeros((250,303),dtype=np.uint8)


# In[31]:


m,n=im_2.shape
for i in range(1,m-1):
    for j in range(1,n-1):
        s=im_2[i-1,j-1]/9+         im_2[i-1,j]/9+          im_2[i,j+1]/9+          im_2[i,j-1]/9+          im_2[i,j]/9+          im_2[i,j+1]/9+           im_2[i+1,j-1]/9+          im_2[i+1,j]/9+            im_2[i+1,j+1] /9   
        s=int(s)
        #print(s, end=' * ')


# In[32]:


plt.subplot(1,2,1)
plt.imshow(im_2,cmap='gray')

plt.subplot(1,2,2)
plt.imshow(im_3,cmap='gray')


# In[ ]:




