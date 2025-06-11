import sys
print(sys.getrecursionlimit())
print(sys.version)
sys.setrecursionlimit(10)  # Set a higher recursion limit if needed
print(sys.getrecursionlimit())

def my_print(i):
    print("Hello, World " + str(i))
    my_print(i+1)  # Recursive call to the same function
# Note: This function will cause infinite recursion and eventually a stack overflow error.


my_print(1)  # Call the function to print "Hello, World!"