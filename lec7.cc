#include <iostream>
 using namespace std;

double func(double x) {
 return x*x -9;
}

double diffunc(double x){
	return 2*x;
}

int main()
{
	double x=1; 
for ( int i=0; i<100; i++){
     x = x - func(x)/diffunc(x);
}
cout << x << endl;
}



	
