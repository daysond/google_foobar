"""
Given a list of elevator versions represented as strings, write a function solution(l) that returns the same list sorted in ascending order by major, minor, and revision number so that you can identify the current elevator version. The versions in list l will always contain major numbers, but minor and revision numbers are optional. If the version contains a revision number, then it will also have a minor number.

For example, given the list l as ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"], the function solution(l) would return the list ["1.0", "1.0.2", "1.0.12", "1.1.2", "1.3.3"]. If two or more versions are equivalent but one version contains more numbers than the others, then these versions must be sorted ascending based on how many numbers they have, e.g ["1", "1.0", "1.0.0"]. The number of elements in the list l will be at least 1 and will not exceed 100.


Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Python cases --
Input:
solution.solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"])
Output:
    0.1,1.1.1,1.2,1.2.1,1.11,2,2.0,2.0.0

Input:
solution.solution(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"])
Output:
    1.0,1.0.2,1.0.12,1.1.2,1.3.3

"""

from functools import cmp_to_key

def solution(l):
    l.sort(key=cmp_to_key(cmp))
    return l
    
def cmp(lhs, rhs):
    lhs = [int(x) for x in lhs.split(".")]
    rhs = [int(x) for x in rhs.split(".")]
    
    # different major
    if(lhs[0] < rhs[0]):
        return -1
    elif(lhs[0] > rhs[0]):
        return 1
    
    # same major
    ## filling with -1
    while len(lhs) < 3:
        lhs.append(-1)
    
    while len(rhs) < 3:
        rhs.append(-1)
    
    # camparing minor
    if(lhs[1] < rhs[1]):
        return -1
    elif(lhs[1] > rhs[1]):
        return 1
    elif(lhs[2] < rhs[2]):
        return -1
    elif(lhs[2] > rhs[2]):
        return 1
    else:
        return 0

# test cases
    
t = solution(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"])
print(t)

t = solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"])
print(t)

t = solution(["1.0", "1", "1.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"])
print(t)

## not my solution

def solution2(l):
    # Convert each version string into a tuple of integers for easy comparison
    version_tuples = [tuple(map(int, v.split('.'))) for v in l]
    
    # Sort the list of version tuples, considering the length of each version tuple for tie-breaking
    sorted_versions = sorted(version_tuples, key=lambda x: (x + (0,)*3)[:3] + (len(x),))
    
    # Convert the sorted version tuples back into strings
    sorted_version_strings = ['.'.join(map(str, v)) for v in sorted_versions]
    
    return sorted_version_strings


## Inspired solution
def solution3(l):
    l.sort(key=lambda x: (tuple(map(int, x.split('.'))) + (-1,)*(3 - len(x))))
    return l



from profiler import profiler 

repeat = 1000000

profiling = profiler(solution, repeat)
profiling(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]) 

profiling = profiler(solution2, repeat)
profiling(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]) 

profiling = profiler(solution3, repeat)
profiling(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]) 

"""
solution called 1000000 times took 3.4177892208099365 seconds in total.
solution2 called 1000000 times took 4.0579071044921875 seconds in total.
solution3 called 1000000 times took 2.003891706466675 seconds in total.
"""