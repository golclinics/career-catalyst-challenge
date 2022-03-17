#python program to add two numbers using a function

def add_num(a,b):#function for addition
    sum=a+b;
    return sum; #return value
num1=int(input("Enter the first value: "))#input from user for num1
num2=int(input("Enter the second value: "))#input from user for num2

print("The sum is",add_num(num1,num2))#call the function

