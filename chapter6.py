# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 20:52:52 2016

@author: xmuzzy
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def fibs(num):
    result=[0,1]
    for i in range(num-2):
        result.append(result[-2]+result[-1])
    return result

def square(x):
    'calculates the square of the number x'
    return x*x
    
    