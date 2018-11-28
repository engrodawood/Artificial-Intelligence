# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 14:57:08 2017

@author: afsar
"""
import numpy as np
import time
import math
N = 10000
Q = 14
s0 = []
v0 = np.inf
# Set initial temp
temp = 100

#Cooling rate
coolingRate = 0.06;

def acceptanceProbability(oldVal,curVal,temp):
    if curVal < oldVal:
        return 1.0
    else:
         # If the new solution is worse, calculate an acceptance probability
        return math.exp((oldVal - curVal) / temp);

def objFun(boardPos):
    attackingQueen=0
    for i in range(Q):
        m=1
        for j in range(i+1,Q):
            if(abs(boardPos[j]-boardPos[i])==m):
                attackingQueen+=1
            m+=1
    return attackingQueen
    

    
start_time=time.clock()
for i in range(1,N):
    s = np.random.choice(range(Q), Q, replace=False)
    v = objFun(s)
    if(acceptanceProbability(v0,v,temp)>np.random.uniform(0,1)):
        v0 = v
        s0 = s
    if v0 == 0:
        break
    # cooling system
    
    temp*=(1-coolingRate)
end_time=time.clock()


print ("Queens Attacking : ", v0, "\n\nFormation : ", s0 ,"\n\n  Time Elapsed ",end_time-start_time)