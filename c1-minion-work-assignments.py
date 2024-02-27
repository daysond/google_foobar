"""
Minion Work Assignments
=======================
Commander Lambda's minions are upset! They're given the worst jobs on the whole space station, and some of them are starting to complain that even those worst jobs are being allocated unfairly. If you can fix this problem, it'll prove your chops to Commander Lambda so you can get promoted!

Minions' tasks are assigned by putting their ID numbers into a list, one time for each day they'll work that task. As shifts are planned well in advance, the lists for each task will contain up to 99 integers. When a minion is scheduled for the same task too many times, they'll complain about it until they're taken off the task completely. Some tasks are worse than others, so the number of scheduled assignments before a minion will refuse to do a task varies depending on the task. You figure you can speed things up by automating the removal of the minions who have been assigned a task too many times before they even get a chance to start complaining.

Write a function called solution(data, n) that takes in a list of less than 100 integers and a number n, and returns that same list but with all of the numbers that occur more than n times removed entirely. The returned list should retain the same ordering as the original list - you don't want to mix up those carefully-planned shift rotations! For instance, if data was [5, 10, 15, 10, 7] and n was 1, solution(data, n) would return the list [5, 15, 7] because 10 occurs twice, and thus was removed from the list entirely.
"""

"""
Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Python cases --
Input:
solution.solution([1, 2, 3], 0)
Output:
    

Input:
solution.solution([1, 2, 2, 3, 3, 3, 4, 5, 5], 1)
Output:
    1,4
"""
import time

def solution(data, n): 
    # Your code here
    
    if n == 0:
        data.clear()
    else:
        indices = {}
        count = 0
        # getting all indices 
        for idx , num in enumerate(data): # n
            if num in indices:
                indices[num].append(idx)
            else:
                indices[num] = [idx]
        
        for l in indices.values(): # n
            if len(l) > n:
                for idx in l:
                    count += 1
                    data[idx] = None
        
        for i in range(count):
            data.remove(None)
        
    return data

def solution2(data, n): 
    if n == 0:
        data.clear()
    else:
        counts = {}
        for num in data: # n
            counts[num] = counts.get(num, 0) + 1
        
        for num, count in counts.items(): # n
            if count > n:
                for i in range(count):
                    data.remove(num)
    return data

def solution_in_place(data, n):
    # Count the occurrences of each number in data
    counts = {}
    for number in data:
        counts[number] = counts.get(number, 0) + 1
    
    # Remove elements from data that occur more than n times
    # Iterate in reverse to avoid skipping elements due to indexing changes
    for i in range(len(data) - 1, -1, -1):
        if counts[data[i]] > n:
            del data[i]
    
    return data




# Modifying the profile_function to measure the execution time of a function called multiple times

def profile_function_repeated(func, repetitions):
    """
    A function to measure the execution time of a function called repeatedly.
    
    Args:
    - func: The function to be profiled.
    - repetitions: The number of times to execute the function.
    
    Returns:
    The total execution time for all repetitions.
    """
    def wrapper(*args, **kwargs):
        total_time = 0  # Total execution time
        for _ in range(repetitions):
            start_time = time.time()  # Start time before function execution
            func(*args, **kwargs)  # Execute the function
            end_time = time.time()  # End time after function execution
            total_time += (end_time - start_time)  # Accumulate execution time
        avg_time = total_time / repetitions
        print(f"{func.__name__} called {repetitions} times took {total_time} seconds in total.")
        # print(f"Average time per call: {avg_time} seconds.")
        return total_time
    
    return wrapper

# Example function to be profiled
def example_function_to_repeat(n):
    """
    Another example function that calculates the sum of numbers from 1 to n.
    """
    return sum(range(1, n + 1))

# Profiling the example function to repeat it 1000000 times
# Note: Calling the profiler directly with a function and repetition count

repeat = 20000000

profiler = profile_function_repeated(solution_in_place, repeat)
profiler([1, 2, 2, 3, 3, 3, 2, 4, 1, 5, 5], 2)  

profiler = profile_function_repeated(solution2, repeat)
profiler([1, 2, 2, 3, 3, 3, 2, 4, 1, 5, 5], 2)  

profiler = profile_function_repeated(solution, repeat)
profiler([1, 2, 2, 3, 3, 3, 2, 4, 1, 5, 5], 2)  