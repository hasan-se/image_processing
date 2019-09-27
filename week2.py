#!/usr/bin/env python
# coding: utf-8

# In[76]:


import os 


# In[77]:


os.getcwd()  #çalıştığımız dizini göster


# In[78]:


def my_function_1(my_list=[9,3,5,6,2,3,6]):
    for i in range(len(my_list)):
        my_list[i] = my_list[i] +1
    print(my_list)
    


# In[79]:


my_function_1()


# In[80]:


my_list_1 = np.array(([9,3,5,6,2,3,6]))  #ndarray
my_list_1


# In[81]:


my_list_1 +1   #tanımlamalara uygun olmalı int türünden toplama olacak
#liste iki tane pointer kullanıyor , array tek pointer kulllanıyor


# In[82]:


def my_function_2(my_array = np.array(list([9,3,5,6,2,3,6]))):
    return my_array +5
#my_fnction_1(['bir',2,3,5,54,5,56,6])
my_function_2()


# In[83]:


import matplotlib.pyplot as plt
import numpy as np
im_1 = plt.imread('istanbul_goruntu_isleme.jpg')
plt.imshow(im_1)   #im_1.ndim, im_1.shape
plt.show


# In[84]:


def my_function_3(im_100,s=5):
    #s burda işlem yapılcak pixel sayısı , ve s'in default degeri 5
    im_1 = im_100
    
    m,n,p = im_1.shape
    im_2=np.zeros((m,n,3),dtype=int)
    m,n,im_2.shape
    for m in range(im_1.shape[0]):
        for n in range(im_1.shape[1]):
            im_2[m,n,0]=im_1[m,n,0] + s
            im_2[m,n,1]=im_1[m,n,0]
            im_2[m,n,2]=im_1[m,n,0]
    return im_100


# In[86]:



plt.imshow(im_2)
plt.show 


# In[73]:


def my_function_4(im_500): #bu resmi 4/1 oranında kücültüp hard diske yazıcaz
    
    m,n,p = im_500.shape
    new_m = int(m/2)
    new_n= int(n/2)
    im_600=np.zeros((new_m,new_n),dtype=int) #p degeri yani 3 yok yazmadık
    for m in range(new_m):
        for n in range(new_n):
            s0 = ((im_500[m*2,n*2,0]/3)+(im_500[m*2,n*2,1]/3)+(im_500[m*2,n*2,2]/3))   #bulundugum yerdeki butun rgb degerlerini aldı , integer degerini cok fazla
            #aşmamak icin toplayıp 3 e böldük
            #s1 = (im_500[m,n+1,0]+im_500[m,n+1,1]+im_500[m,n+1,2])/3 #bulundugum pixel 'in' bir sagındaki
            #s3 = (im_500[m+1,n,0]+im_500[m+1,n,1]+im_500[m+1,n,2])/3
            #s2 = (im_500[m+1,n+1,0]+im_500[m+1,n+1,1]+im_500[m+1,n+1,2])/3
            #s=(s0+s1+s2+s3)/4 ## pixel ortalamasını al
            
            im_600[m,n]=int(s0)
            
    return im_600


# In[75]:


im_2 = my_function_4(im_1)
plt.imshow(im_2, cmap='gray')
plt.show(im_2)
#plt.imsave()


# In[106]:


# kendisine gönderilen rgb bir resmi 4/1 oranında kuculterek döndüren fonksiyon

def resmi_kucult(im_7):
    m,n,p = im_7.shape
    new_m = int(m/2)
    new_n= int(n/2)
    im_70=np.zeros((new_m,new_n),dtype=int) #p degeri yani 3 yok yazmadık
    for m in range(new_m):
        for n in range(new_n):
            im_70[m,n,0]=int(im_7[m*2,n*2,0]) #kucuk resimdeki 10.pixel olan bölge diger resimde 20.pixel karsılık geliyor 
            im_70[m,n,1]=int(im_7[m*2,n*2,1]) #bu yüzden 2 ile carpıyoruz
            im_70[m,n,2]=int(im_7[m*2,n*2,2])
        
            
    return im_70


# In[108]:


im_40= resmi_kucult(im_1)
im_400 = resmi_kucult(im_40)
plt.imshow(im_400)


# In[ ]:





# In[ ]:




