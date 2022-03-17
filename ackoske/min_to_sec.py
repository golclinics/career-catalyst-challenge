def convertTime(minutes):
    seconds = minutes * 60
    return seconds
print("Time converter from minutes to seconds")
print("--------------------------------------")
minutes = int(input("What is your time in minutes? "))
print("Your time in seconds is: " , convertTime(minutes) , "seconds \n")
