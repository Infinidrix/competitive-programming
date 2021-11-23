#include <bits/stdc++.h>

using namespace std;

int main(){
    int p, budget, hotels, weeks;;
    while (cin >> p >> budget >> hotels >> weeks){
        int minPrice = INT32_MAX;
        for (int i = 0; i < hotels; i++){
            int price;
            cin >> price;
            for (int j = 0; j < weeks; j++){
                int people;
                cin >> people;
                if (people >= p){
                    minPrice = min(minPrice, p * price);
                }
            }
        }
        if (minPrice > budget){
            cout << "stay home" << '\n';
        } else {
            cout << minPrice << '\n';
        }
    }
}