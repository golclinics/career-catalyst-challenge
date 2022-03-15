# This code implements a function that accepts input in minutes and converts it to seconds
# Written by Paula Musuva

# Function definition
def toSeconds(mins):
    seconds = mins * 60
    return seconds

# Main Program
print ("Welcome to this program that takes a value you input in minutes and converts it to seconds")
inMinutes = input("Enter value in minutes: ")
outSeconds = toSeconds(inMinutes)
print (f"{inMinutes} minutes is {outSeconds} seconds")