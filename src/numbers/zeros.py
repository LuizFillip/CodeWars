# -*- coding: utf-8 -*-
"""
Created on Tue May  9 23:28:38 2023

@author: Luiz
"""

n = 6
def zeros(n):
    s = 1
    for i in range(1, n + 1):
        s *= i
        
    count = 0
    for j in str(s)[::-1]:
        
        if int(j) != 0:
            break
        else:
            count += 1
        
    return count

n = 100000

def zeros(n):
    """chat"""
    count = 0
    while n >= 5:
        n //= 5
        count += n
    return count

def zeros(n):
  x = n/5
  return x+zeros(x) if x else 0