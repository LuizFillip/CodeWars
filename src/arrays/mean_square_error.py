

arr_a = [1, 2, 3]
arr_b = [4, 5, 6]

def solution(array_a, array_b):
    """
    Complete the function that

    accepts two integer arrays of equal length
    compares the value each member in one array to the corresponding member in the other
    squares the absolute value difference between those two values
    and returns the average of those squared absolute value difference between each member pair.
    """
    return sum([pow(abs(array_b[i] - array_a[i]), 2) 
                for i in range(len(array_a))]) /  len(array_a)




def solution(a, b):
    return sum((x - y)**2 for x, y in zip(a, b)) / len(a)

def tests():
    solution([10, 20, 10, 2], [10, 25, 5, -2] )


    solution([-1, 0], [0, -1])
    