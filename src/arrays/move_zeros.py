import numpy as np

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

def change_position(array, element, new_position = 0):
    
    # Find the index of the element
    index_to_move = np.where(array == element)[0][0]
    
    # Use np.roll to change the position
    return np.roll(array, new_position - index_to_move)
# identify_sequences(df)
