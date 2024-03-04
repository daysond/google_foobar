"""
1) Add one fuel pellet
2) Remove one fuel pellet
3) Divide the entire group of fuel pellets by 2 (due to the destructive energy released when a quantum antimatter pellet is cut in half, the safety controls will only allow this to happen if there is an even number of pellets)

Write a function called solution(n) which takes a positive integer as a string and returns the minimum number of operations needed to transform the number of pellets to 1. The fuel intake control panel can only display a number up to 309 digits long, so there won't ever be more pellets than you can express in that many digits.

For example:
solution(4) returns 2: 4 -> 2 -> 1
solution(15) returns 5: 15 -> 16 -> 8 -> 4 -> 2 -> 1

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Python cases --
Input:
solution.solution('15')
Output:
    5

Input:
solution.solution('4')
Output:
    2

"""

# First solution, didn't passed all the cases
# see pattern in decimal
# when tens digit is odd: turn last digit to 2, 6, 0  e.g 31 -> add 1 -> 32  
#                   even: turn last digit to 4, 8, 0  e.g 41 -> minus 1 -> 40
#                       by adding or subtracting 1.
# except for 3, or when its single digits, only +1 when its 7

def solution0(n):
    numOps = 0
    data = n
    # if even
    while data != '1':
        l = len(data)
        if not int(data)&1:
            data = str(int(data)//2)
            # print(f"data in if {data}")
            numOps += 1
        # if second last digit is odd    
        elif l >= 2 and int(data[-2:]) & 1:
            if data[-1:] in ('1', '5', '9'): 
                data = str((int(data) +1)//2)
            else:
                data = str((int(data) -1)//2) 
            # print(f"data in elif {data}")
            numOps += 2
            
        elif l>=2 and not int(data[-2:]) & 1:
            if data[-1:] in ('1', '5', '9'): 
                data = str((int(data) -1)//2)
            else:
                data = str((int(data) +1)//2) 
            numOps += 2
        else:
            data = str((int(data) + 1)//2) if int(data) == 7 else str((int(data) - 1)//2)
            # print(f"data in else {data}")
            numOps += 2 
    return numOps
# problem: alternating between str and int, division is super slow


# better solution use bitwise to half the value
# see pattern in binary
"""
1: 0001     10: 001010
3: 0011     20: 001000
5: 0101     30: 011110
7: 0111     40: 101000
9: 1001     50: 110010
            60: 111100
            
for the single odd digits: 1, 3, 5, 7, 9, the LSB is always 1, and the second LSB alters between 0 and 1.
for the tens, LSB is 0 because they are even numbers, and the second LSB alters between 0 and 1.
When adding the odd digits and the tens together, the second bit will alter between 0 and 1 as well. The LSB will not affect the second LSB because there will be no carry over. However, the second LSB will alter.
"""

def solution(n):
    numOps = 0
    data = int(n)
    while data != 1:
        if not data & 1:
        # even
            data >>= 1
            numOps += 1
        elif data != 3 and data & 2:
        # if 3, just -1
        # tens place is odd and last digit is 1, 5, 9
        # tens place is even and last digit is 3, 7 
            data += 1
            data >>= 1
            numOps += 2            
        else:
        # tens place is odd and last digit is 3, 7
        # tens place is even and last digit is 1, 5, 9 
            data -= 1
            data >>= 1
            numOps += 2 
            
    return numOps


    
t = solution0('2336756455')  
print(t)

t = solution('2336756455')  
print(t)    

t = solution('1')  
print(t)

t = solution('2')  
print(t)    

t = solution('3')  
print(t)

t = solution('16')  
print(t)    

t = solution('31')  
print(t)   

t = solution('33')  
print(t)   


from profiler import profiler 
repeat = 100000

profiling = profiler(solution0, repeat)
profiling('2336756455') 

profiling = profiler(solution, repeat)
profiling('2336756455') 

