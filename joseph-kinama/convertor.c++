#include <iostream>   
using namespace std;

int convertor(int);

int main(){
   cout<<"1 minute = "<<convertor(1)<<" seconds"<<endl;
   cout<<"2 minute = "<<convertor(2)<<" seconds"<<endl;
   cout<<"60 minute = "<<convertor(60)<<" seconds"<<endl;
}


int convertor(int minutes){
    return minutes*60;
}