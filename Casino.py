#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 19:21:34 2019

@author: batdora
"""

from matplotlib.pyplot import *
import numpy as np


N=np.zeros((10000,1000))
t=np.zeros((10000,1000))
t[0,:]=0
N[0,:]=100


for i in range(0,10000-1):
    t[i+1,:]=t[i,:]+1
    
    """
    Creates an array with random integers between 1 and 0
    """
    R=np.random.rand(1,1000)
    
    """Gets the random integers and converts them ton -1 and +1
    Step 1. Set them as true and false
    (Make False=0 True=1)(inside step 2)
    Step 2. Multiply with 2
    Step 3. Subtract 1
    (You have -1 and +1)!!!!!!
    """
    N[i+1,:]=N[i,:]+(R<0.5)*2-1

plot(t, N)
