#include <iostream>
using namespace std;

// Create a function that takes two numbers as arguments and returns their sum.
int summation(int x, int y) {
  return x + y;
}

int main() {
    // Declaring the variables
    int num1,num2; 
    // Prompting user for first digit
    cout << "Enter the first digit: ";
    cin >> num1;
    // Prompting user for the second digit
    cout << "Enter the second digit ";
    cin>> num2;
    // Display of the result of summation
    cout <<"The sum of both digits is  :"<< summation(num1, num2);
    return 0;
}
