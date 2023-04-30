"""
Your task is to write a function named do_math that receives a single argument. This argument is a string that contains multiple whitespace delimited numbers. Each number has a single alphabet letter somewhere within it.

Example : "24z6 1x23 y369 89a 900b"
As shown above, this alphabet letter can appear anywhere within the number. You have to extract the letters and sort the numbers according to their corresponding letters.

Example : "24z6 1x23 y369 89a 900b" will become 89 900 123 369 246 (ordered according to the alphabet letter)
Here comes the difficult part, now you have to do a series of computations on the numbers you have extracted.

The sequence of computations are + - * /. Basic math rules do NOT apply, you have to do each computation in exactly this order.
This has to work for any size of numbers sent in (after division, go back to addition, etc).
In the case of duplicate alphabet letters, you have to arrange them according to the number that appeared first in the input string.
Remember to also round the final answer to the nearest integer.

"""

def split_string(s):
    dic = []

    for i, string in enumerate(s.split()):
        for letter in string:
            if letter.isalpha():
                number = int(string.replace(letter, ""))
                dic.append((f"{letter}{i}", number))
                
    return [item[1] for item in sorted(dic)]


def plus(num, count): 
    count += num
    return count
def minus(num, count): 
    count -= num
    return count
def times(num, count): 
    count *= num
    return count

def divide(num, count): 
    count /= num
    return count


def operations(length):
    ops_list = [plus, minus, times, divide]
    if length != 4:
        return ops_list * (abs(length - 4))
    else:
        return ops_list

def do_math(s):
    numbers = split_string(s)
    
    ops = operations(len(numbers))
    
    count = numbers[0]
    
    for index, num in enumerate(numbers[1:]):
        count = ops[index](num, count)
        
    return round(count)


def run_test():
    s = "24z6 1x23 y369 89a 900b"
    #s = "24z6 1z23 y369 89z 900b"
    #s = "10a 90x 14b 78u 45a 7b 34y"
    s = "1z 2t 3q 5x 6u 8a 7b"
    s = "845e 166g 1424u 97t"
    
    do_math(s)

