#include <iostream>

using namespace std;

void sum (int number1, int number2);//Function prototype

int main()
{
	int number1, number2;

	//get the two numbers from the user
	cout << "Enter the two numbers to find their sum : " << endl;
	cin >> number1 >> number2;

    sum(number1, number2);//call the function

	return 0; //return value
}
void sum (int num1, int num2)
{
	int sum;
	sum = num1 + num2;

	cout << "The sum of the two numbers is : " << sum << endl;
}

