# Use recursion to show factorial of 8

# 8!

# 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1

def factorial_8(n):

    if n==1:
        return 1
    
    return n * (factorial_8(n-1))


print(factorial_8(8))



