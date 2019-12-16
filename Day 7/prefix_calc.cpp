#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Stack{
	private:
		vector<string> array;
		int array_size = 0;
	public:
		void push(string value){
			array.push_back(value);
			array_size++;
		}
		string pop(){
			string returnable = array[--array_size];
			array.erase(array.end());
			return returnable;
		}
		bool isEmpty(){
			return (array_size == 0);
		}
		int size(){
			return array_size;
		}
		
};

vector<string> toVector(string expr){
	string temp_result = "";
	vector<string> result;
	for(int i = 0; i<expr.size(); i++){
		if (expr.at(i) == '+' or expr.at(i) == '-' or expr.at(i) == '*' or expr.at(i) == '/'){
			if(temp_result != ""){
				result.push_back(temp_result);
				temp_result = "";
			}
			string temp(1, expr.at(i));
			result.push_back(temp);
		}
		else if(expr.at(i) == ' ' or expr.at(i) == ','){
			if(temp_result != ""){
				result.push_back(temp_result);
				temp_result = "";
			}
		}
		else{
			temp_result += expr.at(i);
		}
	}
	if(temp_result != ""){
		result.push_back(temp_result);
	}
	return result;
}
int eval(vector<string> expr){
	Stack expr_stack;
	Stack operands;
	int list_size = expr.size();
	for (int i = 0; i < list_size; i++){
		expr_stack.push(expr[i]);
	}
	while (!expr_stack.isEmpty()){
		string oper = expr_stack.pop();
		if (oper == "+"){
			string x = operands.pop();
			string y = operands.pop();
			operands.push(to_string(stoi(x) + stoi(y)));
			//cout<<"Adding "<<x<<y<<expr_stack.size()<<endl;
		}
		else if(oper == "-"){
			string x = operands.pop();
			string y = operands.pop();
			operands.push(to_string(stoi(x) - stoi(y)));
			//cout<<"Subtracting "<<x<<y<<expr_stack.size()<<endl;
		}
		else if(oper == "*"){
			string x = operands.pop();
			string y = operands.pop();
			operands.push(to_string(stoi(x) * stoi(y)));
			//cout<<"Multiplying "<<x<<y<<" "<<expr_stack.size()<<endl;
		}
		else if(oper == "/"){
			string x = operands.pop();
			string y = operands.pop();
			operands.push(to_string(stoi(x) / stoi(y)));
			//cout<<"Dividing "<<x<<y<<expr_stack.size()<<endl;
		}
		else{
			operands.push(oper);
		}
	}
	return stoi(operands.pop());
}


int main(){
	string hi;
	hi = "+4*3 12";
	cout<<eval(toVector(hi))<<endl;
	string test;
	cin>>test;
	cout<<eval(toVector(test))<<endl;
}