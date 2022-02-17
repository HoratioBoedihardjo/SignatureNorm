#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Code is minor modification of one by Louis
import math
import iisignature
import matplotlib
import numpy
from itertools import product

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt

n=3
T= 1.
times = np.linspace(0., T, n)
dt = times[1]-times[0]
dB = np.sqrt(dt)*np.random.normal(size=(n-1,))
dB1 = np.sqrt(dt)*np.random.normal(size=(n-1,))
B0 = np.zeros(shape=(1,))
B=np.concatenate((B0, np.cumsum(dB,))).reshape((-1,1))
B1=np.concatenate((B0, np.cumsum(dB1))).reshape((-1,1))

BPath = np.append(B,B1, axis=1)

sig1 =iisignature.sig(BPath, int(16-1))
sig2 =iisignature.sig(BPath, int(16))
siglevel = np.array([j for j in sig2 if j not in sig1])

list1 = ['00', '11']
norm=[]
for e1,e2,e3,e4,e5,e6,e7,e8 in product(list1, repeat=8):
    norm.append(siglevel[int(e1+str(e2)+str(e3)+str(e4)+str(e5)+str(e6)+str(e7)+str(e8),2)])

normsum = np.sum(norm)
normlength = abs(normsum)

l = math.factorial(16)*(normlength)
result = math.pow(l,float(1)/float(16))



dBsq = dB**(2)
dB1sq = dB1**(2)
sq = dBsq + dB1sq
elements = np.sqrt(sq)
length = np.sum(elements)

print(length)
print(result)

