# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 18:37:12 2023

@author: Luiz
"""

class narcissistic:
    
    def func1( value ):
        base = len(str(value))
    
        nums = list(map(int,str(value)))
    
        if sum([pow(i, base) for i in nums]) == value:
            return True
        else:
            return False
    
    
    def func2(value):
        return value == sum(int(x) ** len(str(value))
                            for x in str(value))
    
    def test():
        value = 153
        value = 371
        value = 7
        value = 122
        value = 4887
        
        narcissistic(value)