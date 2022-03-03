# function
def convert(min):
    return min*60

# test value 
print("5 mins: " + str(convert(5)) + " seconds")
print("3 mins: " + str(convert(3)) + " seconds")


# prompt user to enter value
minutes = input("Enter minutes to convert to seconds: ")

print(convert(int(minutes)))