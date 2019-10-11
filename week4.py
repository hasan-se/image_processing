#!/usr/bin/env python
# coding: utf-8

# In[30]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt
data_path = "C:/Users/TheSesli/"
train_data = np.loadtxt(data_path + "mnist_train.csv", delimiter=",")
                        
test_data = np.loadtxt(data_path + "mnist_test.csv", delimiter=",")

image_size = 28 # width and length
image_pixels = image_size * image_size


# In[39]:


train_data.ndim, train_data.shape #785 = 28*28 + 1
train_data[10,0]  # 10.satırda hangi digit olduğunu yazar

im_3 = train_data[10,:0] #0 da 3 olduğuna karar verdikten sonra

im_4 = im_3[1:]
im_4.shape
#im_5 = im_4.reshape(28,28)
plt.imshow(im_4, cmap='gray')
plt.show()


# In[ ]:


#train data set üzerinde kaç tane 3 var??
60000 , 785 ; 1 +28*28 #60000 tane digit var her bir resimde 758 pixel var 


# In[ ]:


m,n = train_data.shape
m,n


# In[ ]:


def my_counter(k=0):
    s=0
    for i in range(m):
        if(train_data[i:0]==3): #i. satırda digit 3 mü
            s=s+1
        
    return s


# In[ ]:


my_counter(4)


# In[33]:


import math

def my_pdf_1(x, mu=0.0, sigma=1.0):
    x = float(x - mu) / sigma
    return math.exp(-x*x/2.0) / math.sqrt(2.0*math.pi) / sigma


# 

# In[34]:


# digit 0 olan karenin pixelinin en üst kısmı kaç min ve varyansını hesapla
def get_my_mean_and_std(k=0,l=0):
    m,n = train_data.shape
    m,n
    s=0 #kac tane oldugu
    t=0 #toplam
    k=0 #sınıf bilgisi
    l=350 #nolu locantion olan indensity degeri
    for i in range(m):
        if(train_data[i,0]==k):
            s=s+1
            t=t + train_data[i,l+1]
            #digit_class = train_data[i,0]
            #top_left = train_data[i,1] #pixel deki intensity degeri
            #bottom_right = train_data[i,784]
            #print(digit_class,end=" ")
            #print(top_left,end=" ")
            #print(bottom_right,end=" \n")
    mean_1 = t/s
    s,t=0,0 
    for i in range(m):
        if(train_data[i,0]==k):
            s=s+1
            diff_1 = train_data[i,l+1] -mean_1
            t=t+ (diff_1*diff_1)


    std_1=np.sqrt(t/(s-1))
    return mean_1,std_1
    


# In[ ]:





# In[35]:


my_1,std_1=get_my_mean_and_std(2,100)
my_pdf_1(40,my_1,std_1)


# In[ ]:




