def hello():
    print("Hello, World!")

def pack(a, b, c):
   return [a, b, c]

print(pack(1, 2, 3))

def eat_lunch(lunch_list):
    
    for i in lunch_list:
        if len(lunch_list) == 0:
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

