#include <iostream>

using namespace std;

int main(){
	int array[] = {1, 4, 2, 6, 3, 6, 7, 2, 5, 9, 11, 0};
	int size = (sizeof(array)/sizeof(*array));
	int range_begin = 0;
	int range_end = 12;
	int return_array[size] = {0};
	int count_array[range_end - range_begin] = {0};
	for (int i = 0; i<size; i++){
		count_array[array[i]]++;
	}
	for (int i = 1; i<size; i++){
		count_array[i] += count_array[i-1];
	}
	for (int i = size-1; i>0; i--){
		return_array[--count_array[array[i]]] = array[i];
	}
	for (int i = size-1; i>0; i--){
		cout<<return_array[i]<<endl;
	}
}