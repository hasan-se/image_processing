#!/usr/bin/env python
# coding: utf-8

# In[41]:


import matplotlib.pyplot as plt
import numpy as np ## kovaryans fonksiyonu bu kütüphanede


# In[42]:


x=[180,170,170,175,181,175,177,185,179,160]
y=[95,70,60,79,60,63,83,80,75,50]
x,y,len(x),len(y)
X = np.stack((x, y), axis=0)
X
sigma_1=np.cov(X)  #x,y varyansını aldık sigma_1
sigma_1


# In[43]:


def generate_data():
    x=[180,170,170,175,181,175,177,185,179,160]
    y=[95,70,60,79,60,63,83,80,75,50]
    X = np.stack((x, y), axis=0)
    return X


# In[44]:


def get_cov_matrix(X):
    X = np.stack((x, y), axis=0) 
    sigma_1=np.cov(X)
    return sigma_1


# In[45]:


data_1=generate_data()
get_cov_matrix(data_1)


# In[46]:


def multivariate_normal(x , d, mean, covariance):
    x_m= x - mean
    return (1. / (np.sqrt((2 * np.pi)**d * np.linalg.det(covariance))) *
             np.exp(*(np.linalg.solve(covariance, x_m).T.dot(x_m))/ 2 ))


# In[58]:


x=generate_data()
np.mean(x[0,:]),np.mean(x[1,:])
x_1=[175,72]
d_1=2
data=generate_data()
mean_1=np.array([np.mean(x[0,:]),np.mean(x[1,:])])
covariance_1=get_cov_matrix(data)
multivariate_normal(x_1,d_1,mean_1,covariance_1)


# In[57]:


for i in range(10):
    v=164+i
    x_1=[v,72]
    s=multivariate_normal(x_1,d_1,mean_1,covariance_1)
    print(v,"        ",s)


# In[ ]:




