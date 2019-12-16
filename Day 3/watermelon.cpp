#include <iostream>

using namespace std;

int main(){
	int weight;
	cin>>weight;
	if (weight % 2 == 0 && weight >= 4){
		cout<<"YES";
	}
	else{
		cout<<"NO";
	}
	cout<<endl;
	return 0;
}