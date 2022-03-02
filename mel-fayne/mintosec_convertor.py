# Entry Challenge V3
# Write a function ( myFunction (){} ) that takes an integer minutes and converts it to seconds.


def min_convertor () :
    try:
        min = int(input("Enter number of minutes : "))
        sec = int(min) * 60
        print("\nResult : {} minutes is equal to {} seconds.\n".format(min, sec))
    except ValueError:
        print("Invalid input! Please enter an valid number e.g. 33, 2345")
    

min_convertor()
while True:
    answer = None
    while answer not in ("y", "n"): 
        answer = input("Would you like to continue? (y or n) ") 
        if answer == "y": 
            min_convertor()
        elif answer == "n": 
            print("Thank you for using the min to sec convertor :)") 
            break   
        else: 
            print("\n Please enter y for yes or n for no!\n") 
    if answer == 'n':
        break