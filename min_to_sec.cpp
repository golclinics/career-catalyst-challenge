#include<iostream>
using namespace std;
int results(int min);
int main(){
	int minutes,seconds;
	cout<<"Enter the number of minutes\n";
	cin>>minutes;
	
	seconds=results(minutes);
	cout<<"The number of seconds is :"<<seconds;
	return 0;
	
}
int results(int min)
{
	return(min*60);
}

