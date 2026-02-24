#Juro Uhlík pozdravuje

import numpy as np
import matplotlib.pyplot as plt
import random as rd
from skimage import io
import skimage.io

y1=1250
y2=1750
x1=300
x2=800

image_stack = skimage.io.imread('https://github.com/guiwitz/PyImageCourse_beginner/raw/master/images/46658_784_B12_1.tif')
image_nuclei = image_stack[x1:x2,y1:y2,2]  

X = x2 - x1
Y= y2 - y1

x=20
y=20

a=[]
for i in range(20*20):
    a.append(0)
kerk=np.array(a)  
kerk=kerk.reshape(20,20)
kerk[10,10]=255






def randomdots(n, kerk):
    for i in range(n):
        kerk[rd.randint(0,19),rd.randint(0,19)]= 255
    return kerk
        


def meansmoothing(kerk):
    #going through the map
    finalkerk=kerk.copy()

    for yy in range(1,19):
        for z in range(1,19):
            arr = kerk[yy-1:yy+2, z-1:z+2].copy()     
        
        #averaging
            a=0
            for y in range(3):
                for x in range(3):
                    a=a+arr[x,y]
            av=a/9
            finalkerk[yy, z] =av
    
    finalkerk[10,10]=100

    return finalkerk

def gaussianmoothing(kerk,X,Y):
    #going through the map
    finalkerk=kerk.copy()

    for yy in range(1,Y-1):
        for z in range(1,X-1):
            arr = kerk[yy-1:yy+2, z-1:z+2].copy()
            gaus=np.array([
                [1,4,1],
                [4,16,4],
                [1,4,1]
            ])
            arr=arr*gaus
        #averaging
            a=0
            for y in range(3):
                for x in range(3):
                    a=a+arr[x,y]
            av=a/(36) #normalized by the sum of the Gaussian kernel 
            finalkerk[yy, z] =av
    kerk=finalkerk.copy()
    
    finalkerk[10,10]=100   #just so it has stable reference point
    return finalkerk
    



image_stack = skimage.io.imread('https://github.com/guiwitz/PyImageCourse_beginner/raw/master/images/46658_784_B12_1.tif')
image_nuclei = image_stack[y1:y2,x1:x2,2]  

noisy = 20*np.random.rand(20,20)

randomdots(50, kerk)

plt.imshow(meansmoothing(noisy), cmap='gray')
plt.show()
plt.imshow(gaussianmoothing(noisy, x, y), cmap='gray')
plt.show()
plt.imshow(gaussianmoothing(image_nuclei,X,Y), cmap='gray')
plt.show()

