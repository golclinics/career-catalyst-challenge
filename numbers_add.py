print("Hey there")


#function
def add_numbers(y,z):
sum_of_numbers = y + z
    return sum_of_numbers;

#program
if __name__ == "__main__":
y = float(input("Enter your first number: ").strip())
z = float("Enter your second number: ").strip()
added = add_numbers(y,z)
print("Hey, your number is",added)

