#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Detection---Car-and-Pedestrian-using-OpenCV" data-toc-modified-id="Detection---Car-and-Pedestrian-using-OpenCV-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Detection - Car and Pedestrian using OpenCV</a></span><ul class="toc-item"><li><span><a href="#Pedistrian-Detection" data-toc-modified-id="Pedistrian-Detection-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Pedistrian Detection</a></span></li><li><span><a href="#Car-Detection" data-toc-modified-id="Car-Detection-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Car Detection</a></span></li></ul></li></ul></div>

# ## Detection - Car and Pedestrian using OpenCV
# 

# In[3]:


import sys
print(sys.executable)


# ### Pedistrian Detection

# In[6]:


import cv2
import numpy as np

# Body classifier
body_classifier = cv2.CascadeClassifier('Haarcascades\haarcascade_fullbody.xml')

# Initiate video capture for video file
video = cv2.VideoCapture('images/walking.avi')

# Loop once video is successfully loaded
while video.isOpened():
    
    # Read first frame
    ret, frame = video.read()
    frame = cv2.resize(frame, None,fx=0.5, fy=0.5, interpolation = cv2.INTER_LINEAR)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Pass frame to our body classifier
    bodies = body_classifier.detectMultiScale(gray, 1.2, 3)
    
    # Extract bounding boxes for any bodies identified
    for (x,y,w,h) in bodies:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
        cv2.imshow('Pedestrians', frame)

    if cv2.waitKey(1) == 13: #13 is the Enter Key
        break

video.release()
cv2.destroyAllWindows()


# ### Car Detection
# 

# In[7]:


import cv2
import time
import numpy as np

# Car classifier
car_classifier = cv2.CascadeClassifier('Haarcascades\haarcascade_car.xml')

# Initiate video capture for video file
video = cv2.VideoCapture('images/cars.avi')


# Loop once video is successfully loaded
while video.isOpened():
    
    time.sleep(.05)
    # Read first frame
    ret, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   
    # Pass frame to our car classifier
    cars = car_classifier.detectMultiScale(gray, 1.4, 2)
    
    # Extract bounding boxes for any bodies identified
    for (x,y,w,h) in cars:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
        cv2.imshow('Cars', frame)

    if cv2.waitKey(1) == 13: #13 is the Enter Key
        break

video.release()
cv2.destroyAllWindows()


# 
