# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 18:38:33 2023

@author: Luiz
"""

def move_zeros(lst):
    """
    Write an algorithm that takes an array and moves all of 
    the zeros to the end, preserving the order of the other 
    elements.
    """
    
    begin = []
    end = []
    for num in lst:
        if num == 0:
            end.append(num)
        else:
            begin.append(num)
            
    return begin + end

lst = [1, 0, 1, 2, 0, 1, 3] # returns [1, 1, 2, 1, 3, 0, 0]

def move_zeros(arr):
    l = [i for i in arr if isinstance(i, bool) or i!=0]
    return l+[0]*(len(arr)-len(l))
