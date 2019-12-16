#include <iostream>
#include <sstream>
#include <string>

using namespace std;

//The computer this was tested on did not support to_string therefore the implementation of big_adder was taken to python on day 2

int intify(string num1){
    stringstream num_to_be(num1);
    int returnable;
    num_to_be >> returnable;
    return returnable;
}
void add(string num1, string num2){
	int bigger_num, smaller_num;
	if (num1.size() < num2.size()){
		bigger_num = num2.size();
		smaller_num = num1.size();
	}
	else{
		smaller_num = num2.size();
		bigger_num = num1.size();
	}
	string prefix = "";
	string prefix2 = "";
	if (num1.at(0) == '-'){
		prefix = "-";
	if (num2.at(0) == '-'){
		prefix2 = "-";
	string sum = "";
	int carry = 0;
	for(int i=0; i<bigger_num; i++){
		string temp1, temp2;
		if (i<smaller_num){
			temp1 = prefix + num1.at(num1.size()-i);
			temp2 = prefix2 + num2.at(num2.size()-i);
		}
		else{
			if (num1.size() < num2.size()){
				temp1 = "0";
				temp2 = prefix2 + num2.at(num2.size()-i);
			}
			else{
				temp1 = prefix + num1.at(num1.size()-i);
				temp2 = "0";
			}
		}
		int sum_p = intify(temp1) + intify(temp2) + carry;
		if (sum_p<0){
			sum = to_string(sum_p + 10) + sum;
			carry = -1;
		}
		else if(sum_p>=10){
			sum = to_string(sum_p - 10) + sum;
			carry = 1;
		}
		else{
			sum = to_string(sum_p) + sum;
			carry = 0;
		}
	}
	if (carry == 1){
		sum = "1" + sum;
	}
	else if (carry == -1){
		sum = "-" + sum;
	}
	cout<<sum;
}
int main(){
	string num1, num2;
	cin>>num1>>num2;
	add(num1, num2);
}
