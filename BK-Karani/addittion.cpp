#include<iostream>
using namespace std;
int addition(int num1, int num2);
int main (){
	int num1;
	int num2;
	int sum;
	cout<<"Enter first number:"<<endl;
	cin>>num1;
	cout<<"Enter second number:"<<endl;
	cin>>num2;
	
	sum=addition(num1,num2);
	cout<<"Addittion is:"<<sum<<endl;
	return 0;
}
int addition(int num1, int num2)
{

    return (num1+num2);
}
