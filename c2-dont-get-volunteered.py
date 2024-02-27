"""
Don't Get Volunteered!
======================
As a henchman on Commander Lambda's space station, you're expected to be resourceful, smart, and a quick thinker. It's not easy building a doomsday device and ordering the bunnies around at the same time, after all! In order to make sure that everyone is sufficiently quick-witted, Commander Lambda has installed new flooring outside the henchman dormitories. It looks like a chessboard, and every morning and evening you have to solve a new movement puzzle in order to cross the floor. That would be fine if you got to be the rook or the queen, but instead, you have to be the knight. Worse, if you take too much time solving the puzzle, you get "volunteered" as a test subject for the LAMBCHOP doomsday device!

To help yourself get to and from your bunk every day, write a function called solution(src, dest) which takes in two parameters: the source square, on which you start, and the destination square, which is where you need to land to solve the puzzle. The function should return an integer representing the smallest number of moves it will take for you to travel from the source square to the destination square using a chess knight's moves (that is, two squares in any direction immediately followed by one square perpendicular to that direction, or vice versa, in an "L" shape). Both the source and destination squares will be an integer between 0 and 63, inclusive, and are numbered like the example chessboard below:

-------------------------
| 0| 1| 2| 3| 4| 5| 6| 7|
-------------------------
| 8| 9|10|11|12|13|14|15|
-------------------------
|16|17|18|19|20|21|22|23|
-------------------------
|24|25|26|27|28|29|30|31|
-------------------------
|32|33|34|35|36|37|38|39|
-------------------------
|40|41|42|43|44|45|46|47|
-------------------------
|48|49|50|51|52|53|54|55|
-------------------------
|56|57|58|59|60|61|62|63|
-------------------------

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit Solution.java

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Python cases --
Input:
solution.solution(19, 36)
Output:
    1

Input:
solution.solution(0, 1)
Output:
    3
"""


from collections import deque

def solution(src, dest):
    start = Node(value=src)
    return breadthFirstSearch(start, dest)
    
class Node():

    def __init__(self, value, depth=0):
        self.value = value
        self.depth = depth
        self.children = []
    
    def add_child(self, child):
        self.children.append(child)
        
    def get_children(self):
        return self.children
    
    def __repr__(self):
        """
        Represents the Node as a string for debugging.
        """
        return f"({self.value}, {self.depth})"
        # return f"{self.value}"
        # return f"Node(value={self.value}, children={len(self.children)})"veri

def breadthFirstSearch(start, goal):
    # start: Node goal: int
    frontier = deque()
    explored = set() 
    frontier.append(start)

    while True:
        if not len(frontier): raise Exception("No solution found")
        
        node = frontier.popleft()
        explored.add(node.value)

        if node.value == goal:
            return node.depth
        
        children = getChildren(node)
        
        for child in children:
            if child.value == goal:
                return child.depth
            elif child.value not in explored and child.value not in [node.value for node in frontier]:
                frontier.append(child)

def getChildren(node):
    moves = [-10, +6, -17, +15, -15, + 17, -6, +10]
    start = None
    end = None
    
    children = []
    if node.value % 8 == 0:
        start = 4
    
    if node.value % 8 == 1:
        start = 2
    
    if node.value % 8 == 6:
        end = -2
    
    if node.value % 8 == 7:
        end = -4
        
    return [Node(value = node.value+x, depth=node.depth+1) for x in moves[start:end] if node.value+x >= 0 and node.value+x < 64]


from queue import Queue

def minKnightMoves(src, dest):
    # Board size for a standard chessboard
    n = 8
    # Directions a knight can move
    dx = [2, 1, -1, -2, -2, -1, 1, 2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]
    
    # Convert board linear index to 2D coordinates
    src_x, src_y = src // n, src % n
    dest_x, dest_y = dest // n, dest % n
    
    # Queue for BFS
    q = Queue()
    q.put((src_x, src_y, 0))  # (x, y, distance)
    
    visited = set()
    visited.add((src_x, src_y))
    
    while not q.empty():
        x, y, dist = q.get()
        
        # If destination is reached
        if x == dest_x and y == dest_y:
            return dist
        
        # Explore all next moves
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                visited.add((nx, ny))
                q.put((nx, ny, dist + 1))


test_cases = [
    (0, 1), (0, 7), (0, 8), (0, 15),
    (0, 6), (0, 9), (0, 14), (0, 48),
    (0, 62), (7, 15), (7, 0), (56, 0),
    (56, 63), (63, 56), (63, 7), (27, 36),
    (18, 33), (45, 10), (19, 3), (2, 29)
]


# test_cases_with_moves = [(src, dest, minKnightMoves(src, dest)) for src, dest in test_cases]
# print(test_cases_with_moves)

import time

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

repeat = 100000

profiler = profile_function_repeated(solution, repeat)
profiler(7, 15) 

profiler = profile_function_repeated(minKnightMoves, repeat)
profiler(7, 15)  

 


