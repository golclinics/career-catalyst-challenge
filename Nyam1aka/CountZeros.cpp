#include < iostream >
using namespace std;
//A function to add two numbers.
int intAddition(int a,int b)
{
    int sum=a+b;
    return sum;
}
int main()
{
    int a,b;
    cout<<"Enter the first number to be added:";
    cin>>a;
    cout<<"Enter the second number to be added:";
    cin>>b;
    cout<<"The sum of the two numbers is:"<<intAddition(a,b);
    return 0;
}