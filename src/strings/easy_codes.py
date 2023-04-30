# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 18:35:17 2023

@author: Luiz
"""

def pig_it(text):
    """
    Move the first letter of each word to the end of it, then             
    add "ay" to the end of the word. Leave punctuation marks 
    untouched.
    
    text = 'Pig latin is cool'
    text = 'Hello world !' # elloHay orldway !
    text = 'This is my string' #'hisTay siay ymay tringsay'
    """
    out = []
    for word in text.split():
        if word.isalpha():
            out.append(word[1:] + word[0] + "ay")
        else:
            out.append(word)
            
    
    return " ".join(out)

def pig_it2(text):
    return " ".join(x[1:] + x[0] + "ay" if x.isalnum() else x for x in text.split())

def alphanumeric(password):
    if len(password) == 0:
        return False
    else:
        return all([i.isalpha() or 
                    i.isnumeric() for i in password])
    
    