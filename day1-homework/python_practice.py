def hello():
    print("Hello, World!")

def pack(a, b, c):
   return [a, b, c]

print(pack(1, 2, 3))

def eat_lunch(lunch_list):
    
    for i in lunch_list:
        while len(lunch_list) == 0:
            print("My lunchbox is empty")
        else:
            print(f"First I eat {lunch_list[0]}")
            for i in range(len(lunch_list)):
                if i == 0:
                    print(f"First I eat {lunch_list[0]}")
                elif len(lunch_list) > 1:
                    print(f"Next I eat {lunch_list[i]}")
            print("My lunchbox is empty.")
                

            
lst_1 = ["bananas", "cheese"]

hello()
eat_lunch(lst_1)   
# next elements say "Next I eat"
# when no elements , say "My lunchbox is empty"



# Please complete the following functions.


# arb_args - Takes in any number of arguments and prints them one at a time.

def arb_args(*args):
    print(args)



arb_args("a", "b")

def loopy_loop():
   
    crazy_loop_var = 0

    while crazy_loop_var == 0:       
        print("stack overflowwwwww!!!")
# inner_func - Takes in two integers. Two nested functions should perform separate, distinct math operations using the integers. The result of both nested functions should then be added together and printed.
# lunch_lady - Takes in two strings: a student's name and their lunch preference. The function should print both strings. If a lunch preference is not given, "Mystery Meat" should be printed instead.
# sum_n_product - Accepts two integers and returns both the sum and the product.
# alias_arb_args - Should be arb_args but assigned an alias. Remember, variables can hold functions in Python just like they can in JS. Alternatively, you can call a function from inside another function.
# arb_mean - Accepts any number of integers and prints their average.
# arb_longest_string - Accepts any number of strings and returns the longest one.

loopy_loop()