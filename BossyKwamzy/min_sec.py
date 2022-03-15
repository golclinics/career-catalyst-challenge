# Entry Challenge V3
 # Write a function ( myFunction (){} ) that takes an integer minutes and converts it to seconds.


def min_sec():
     try:
         min = float(input("Enter number of minutes : ")) #float so we could convert even half minutes like 2.5 minutes to 150 seconds.
         sec = float(min) * 60
         print("\n {} minutes is {} seconds.\n".format(min, sec))
     except ValueError:
         print("Please enter a number: integer or float")
         
     while True:
        choice = None
        while choice not in ("yes", "no"): 
            choice = input("Would you like to continue? yes or no ") 
            if choice == "yes": 
                min_sec()
            elif choice == "no": 
                print("Thank you for using the minutes to seconds convertor") 
                break   
            else: 
                print("\n Please enter yes or no!\n") 
        if choice == 'no':
            break 

if __name__ == "__main__":
    min_sec()