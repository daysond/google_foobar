profiler = profile_function_repeated(solution_in_place, 10000000)
profiler([1, 2, 2, 3, 3, 3, 2, 4, 1, 5, 5], 1)  

profiler = profile_function_repeated(solution2, 10000000)
profiler([1, 2, 2, 3, 3, 3, 2, 4, 1, 5, 5], 1)  

profiler = profile_function_repeated(solution, 10000000)
profiler([1, 2, 2, 3, 3, 3, 2, 4, 1, 5, 5], 1)  