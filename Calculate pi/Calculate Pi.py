# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 19:26:53 2022

@author: marin
"""

"""
In theory of possibilites Pi can be described as next:
    Randomly hit inside of square which inside has circle
    7 out of 10 times most probably will be inside circle
    and 3 out. So 3 miss out of 10. WIth larger number of trials 
    number will be more like 3.14
"""

import numpy as np
import matplotlib.pyplot as plt
import math

def CreateRandomCoordinates(n):
    # create random n coordinates [xxx,xxx]
    Datas = np.random.rand(n,2)
    # in order to find distance from center of circle more easy, points are shifted
    for i in range(0,n):
        Datas[i][0] = Datas[i][0] - 0.5 
        Datas[i][1] = Datas[i][1] - 0.5 
    return Datas

def IsItInCircle (x,y):
    # pytagora formula for geting distance from point to point
    c = math.sqrt(x*x + y*y)
    if c < 0.5:
        # if distance is lover than 0.5 (diametar of circle) point is inside
        return True
    else:
        return False

def DoMagic (Datas):
    x = []
    y = []
    inside = 0
    # separate x and y for ploting
    for i in range(0,len(Datas)):
        x.append(Datas[i][0])
        y.append(Datas[i][1])
        # get the number of inside points and outside points of circle
        if IsItInCircle(x[i],y[i]) :
            inside = inside + 1
    return x,y,inside

# more point more precise 999_000 points precision is under 0.2%
NumOfPiints = 100
# Create datas
Data = CreateRandomCoordinates(NumOfPiints)
# Get statistic and ploting data
x,y,Inside = DoMagic(Data)
# Points that missed circe
Outside = len(x)-Inside
#Calculation of Pi
CalculatePi =   (Outside/ len(x)) * 10 + 1
print ("calculated pi is " + str(CalculatePi))
# Error of calculation using probability
Error = ((np.pi-CalculatePi)/np.pi)*100
print ("Error of calculation is " + str(Error) + " %")

#Ploting the circle and points to get and idea
if NumOfPiints <= 100:
    theta = np.linspace( 0 , 2 * np.pi , 150 )
    radius = 0.5
     
    a = radius * np.cos( theta )
    b = radius * np.sin( theta )
     
    plt.plot( a, b )
    plt.scatter(x, y)
    plt.show()
