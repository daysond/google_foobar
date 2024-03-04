import time

def profiler(func, repetitions):
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