my_list = [1, 2, 3, 4, 5]
my_set = set(my_list)

# Using in operator with a list (O(n) time complexity)
if 3 in my_list:
    print("3 is in the list")

# Using in operator with a set (O(1) average time complexity)
if 3 in my_set:
    print("3 is in the set")