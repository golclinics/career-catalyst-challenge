#include <iostream>

using namespace std;

int sum(int x, int y){
	int sum= x + y;
	cout<< sum;
	return sum; 
}
int main()
{
	sum(345,243);
	return 0;
}