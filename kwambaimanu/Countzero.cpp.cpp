#include <iostream>
using namespace std;
int add(int, int);
int main()
{
    int a = 5, b = 6, sum;
    sum = add(a, b);
    cout << sum ;
    return 0;
}
int add(int x, int y)
{
    int add;
    add = x + y;
    return add;
}
