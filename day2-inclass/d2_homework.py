# def max_num(lst):
#     return max(lst)

# print(max_num([1, 2, 3]))


def mult_list(lst):
    
    # iteration

    result = 0

    for i in lst:
        # print(i)
        # may need condition re length of list
        print(lst[i] * (lst[i] + 1))

        return result
    # output will be 1 times 4 times 8 times 9

    # I need to access 1

    # multiply by the next item in the list



num_list = [1, 4, 8, 9]    

mult_list(num_list)

