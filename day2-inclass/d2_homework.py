def mult_list(lst):

    if not lst:
        return 1
    else:
        return lst[0] * mult_list(lst[1:])


num_list = [1, 4, 8, 9]    

print(mult_list(num_list))


  






# from functools import reduce

# def mult_list(lst):
    
#     # iteration

#     return reduce(lambda x, y: x*y,lst, 1)


#     # output will be 1 times 4 times 8 times 9

#     # I need to access 1

#     # multiply by the next item in the list



# num_list = [1, 4, 8, 9]    

# print(mult_list(num_list))

# import math

# def mult_list(lst):
    
#     # iteration

#     return math.prod(lst)


#     # output will be 1 times 4 times 8 times 9

#     # I need to access 1

#     # multiply by the next item in the list



# num_list = [1, 4, 8, 9]    

# print(mult_list(num_list))