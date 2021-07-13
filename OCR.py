"""
The Sparks Foundation Internship 
@author: Rudra Pratap Singh 
"""

#!/usr/bin/env python
# coding: utf-8

# # Object Detection / Optical Character Recognition (ORC) Project

# In[12]:


#Install Pytorch
get_ipython().system('pip3 install torch torchvision torchaudio')
#Install EasyOCR
get_ipython().system('pip install easyocr')


# In[13]:


import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np


# # Example 1

# In[14]:


# 1 Now Reading the Images 
IMAGE_PATH = 'typed.jpg'


# In[15]:

reader = easyocr.Reader(['en'] , gpu=False)
result = reader.readtext(IMAGE_PATH)
result


# # 2 Drawing Results

# In[16]:


top_left = tuple(result[0][0][0])
bottom_right = tuple(result[0][0][2])
text = result[0][1]
font = cv2.FONT_HERSHEY_SIMPLEX


# In[17]:


img = cv2.imread(IMAGE_PATH)
spacer = 100
for detection in result: 
    top_left = tuple(detection[0][0])
    bottom_right = tuple(detection[0][2])
    text = detection[1]
    img = cv2.rectangle(img,top_left,bottom_right,(0,255,0),3)
    img = cv2.putText(img,text,(20,spacer), font, 0.5,(0,255,0),2,cv2.LINE_AA)
    spacer+=15
    
plt.imshow(img)
plt.show()


# # Example 2

# In[18]:


# 1 Now Reading the Images 
IMAGE_PATH = 'sign.png'


# In[19]:


reader = easyocr.Reader(['en'] , gpu=False)
result = reader.readtext(IMAGE_PATH)
result


# In[20]:


# Drawing Results
top_left = tuple(result[0][0][0])
bottom_right = tuple(result[0][0][2])
text = result[0][1]
font = cv2.FONT_HERSHEY_SIMPLEX


# In[21]:


img = cv2.imread(IMAGE_PATH)
spacer = 100
for detection in result: 
    top_left = tuple(detection[0][0])
    bottom_right = tuple(detection[0][2])
    text = detection[1]
    img = cv2.rectangle(img,top_left,bottom_right,(0,255,0),3)
    img = cv2.putText(img,text,(20,spacer), font, 0.5,(0,255,0),2,cv2.LINE_AA)
    spacer+=15
    
plt.imshow(img)
plt.show()


# # Thank You so much 
