
# # def countdown_iterative(n):
# #   while n >= 0:  
# #     print(n)
# #     n -= 1

# # # Example Usage
# # countdown_iterative(20)


# # RECURSION

# # with base case

# def count_down(n):

#   #  Base case
#   if n==0:
#      print(n)
#     #   return

#   #  Recursive case
#   else:
#       print(n)
#       count_down(n-1)

# # test case
# count_down(20)



# # # without base case

# # def count_down(n):

# #   #  Base case
# # #   if n==0:
# # #      print(n)
# # #     #   return

# # #   #  Recursive case
# # #   else:
# #       print(n)
# #       count_down(n-1)

# # # test case
# # n=8

# # count_down(20)


# with a one dimensional array


import time

# Recursive Function (Factorial Calculation)
def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n-1)  # The recursive call

# Iterative Function (Factorial Calculation)
def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i  # Update result iteratively
    return result

# Input Value
n = 100

# Measure Recursive Function's Time
start_recursive = time.perf_counter()
result_recursive = factorial_recursive(n)
end_recursive = time.perf_counter()

# Measure Iterative Function's Time
start_iterative = time.perf_counter()
result_iterative = factorial_iterative(n)
end_iterative = time.perf_counter()

# Results and Comparison
print(f"Factorial ({n}) - Recursive: {result_recursive}, Time: {end_recursive - start_recursive:.8f} seconds")
print(f"Factorial ({n}) - Iterative: {result_iterative}, Time: {end_iterative - start_iterative:.8f} seconds")





# with a 2-dimensional array

import time

def sum_recursive(matrix):
    if not matrix:  # Base case: empty list
        return 0
    elif not isinstance(matrix[0], list):  # Base case: single number
        return matrix[0]
    else:
        return sum_recursive(matrix[0]) + sum_recursive(matrix[1:])

# Example Matrix
matrix = [[1, 2, 3], [4, 5], [6, 7, 8]]

start_recursive = time.perf_counter()
recursive_sum = sum_recursive(matrix)
end_recursive = time.perf_counter()

print(f"Recursive Sum: {recursive_sum}, Time: {end_recursive - start_recursive:.8f} seconds")


def sum_iterative(matrix):
    total = 0
    for row in matrix:
        for item in row:
            total += item
    return total

start_iterative = time.perf_counter()
iterative_sum = sum_iterative(matrix)
end_iterative = time.perf_counter()

print(f"Iterative Sum: {iterative_sum}, Time: {end_iterative - start_iterative:.8f} seconds")
