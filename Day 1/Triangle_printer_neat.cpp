#include <iostream>

using namespace std;

void printSpaces(int row, int total){
    for (int i = 0; i < total - row - 1; i++){
        cout<<" ";
    }
}
void printStars(int row){
    for (int i = 0; i < 2*row+1;i++){
        cout<<"*";
    }
    cout<<endl;
}


int main(){
    int n;
    cin>>n;
    for(int row=0; row < n; row++){
        printSpaces(row, n);
        printStars(row);
    }
	cin>>n;
    return 0;
}
