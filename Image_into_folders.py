# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 03:23:48 2017

@author: sree
"""
import pandas as pd
import numpy as np
import shutil as sh
p = 'G:\Ganesh-The_lead\photos'

import glob 

image = glob.glob("G:\\Ganesh-The_lead\\photos\\*.jpg")
len(image)
x=image[2]
x[29:-4]
image_data=pd.read_csv('G:\\Ganesh-The_lead2\\photos.csv', sep=',')

filename=[]
category=[]

filename = image_data['photo_id']
category= image_data['label']

for i in range(0,196279) :
    path = 'G:\\Ganesh-The_lead\\photos\\'
    if category[i]=='food' :
        try:
            sh.copy(path +filename[i]+ ".jpg" , 'G:\\Ganesh-The_lead\\New folder\\food')
        except BaseException: 
            pass
    elif category[i]=='menu' :
        try: 
            sh.copy(path +filename[i]+ ".jpg" , 'G:\\Ganesh-The_lead\\New folder\\menu')
        except BaseException: 
            pass
    elif category[i]=='inside' :
        try:
            sh.copy(path +filename[i]+ ".jpg" , 'G:\\Ganesh-The_lead\\New folder\\inside')
        except BaseException: 
            pass
    elif category[i]=='outside' :
        try:
            sh.copy(path +filename[i]+ ".jpg" , 'G:\\Ganesh-The_lead\\New folder\\outside')
        except BaseException: 
            pass
    elif category[i]=='drink' :
        try:
            sh.copy(path +filename[i]+ ".jpg" , 'G:\\Ganesh-The_lead\\New folder\\drink')
        except BaseException: 
            pass
    else:
        try:
            sh.copy(path +filename[i]+ ".jpg" , 'G:\\Ganesh-The_lead\\New folder\\other')
        except BaseException: 
            pass
    
