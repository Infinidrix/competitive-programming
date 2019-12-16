#include <iostream>

using namespace std;

int main(){
	long long int m, n, a, result, temp;
	cin>>n>>m>>a;
	result = (n/a);
	if (n%a != 0){
		result++;
	}
	temp = (m/a);
	if (m%a != 0){
		temp++;
	}
	cout<<result*temp;
}