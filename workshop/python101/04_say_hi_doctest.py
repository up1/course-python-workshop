#https://docs.python.org/3/library/doctest.html
import doctest

"""
Say hi to a person.
>>> say_hi("Somkiat")
Hi, Somkiat!
"""
def say_hi(name: str) -> str:
    """
    Print a greeting message with the provided name.
    
    Args:
        name (str): The name to greet.
    """
    return f"Hi, {name}!"

if __name__ == "__main__":
    doctest.testmod()  # Run the doctests in this module