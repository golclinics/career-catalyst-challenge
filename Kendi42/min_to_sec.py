def myFunction(minutes):
    seconds=minutes*60
    return seconds


# MAIN
print("This program converts minutes to seconds")
minutes=int(input("Enter a number in minutes: "))
print("Your number in seconds is: " , myFunction(minutes),"s")