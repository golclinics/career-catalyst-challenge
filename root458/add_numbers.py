
# Entry Challenge V1

# Create a function that takes two numbers as arguments 
# and return their sum.

def add_numbers(x, y):
    try:
        return x + y
    except:
        # Return None if argument is non-numeric
        return None

print(add_numbers(5, 11))         # Prints 16
print(add_numbers(7, 28))         # Prints 35
print(add_numbers(-5, 1))         # Prints -4
print(add_numbers(-8.22, 3.22))   # Prints -5.0