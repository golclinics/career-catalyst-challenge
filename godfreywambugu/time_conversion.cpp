
#include <iostream>

//Function to convert minutes to seconds
int convert_to_seconds(int minutes)
{
	int seconds = minutes * 60;
	return seconds;
}


//The main function, execution starts here
int main()
{
	//calling the conversion function
	int myseconds = convert_to_seconds(5);
	std::cout << "5 minutes equals " << myseconds << " seconds" << std::endl;
	return 0;
}
