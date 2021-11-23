#include <iostream>
#include <vector>
using namespace std;

long double comb(int n, int m, vector<long double>& fact){
    return fact[n] / (fact[m] * fact[n - m]);
}

int main(){
    int boys, girls, actors;
    cin >> boys >> girls >> actors;
    vector<long double> fact(max(girls, boys) + 2, 1);
    for (int i = 2; i < fact.size(); i++){
        fact[i] = fact[i-1] * i;
    }
    long double ways = 0;
    long double boy_comb = 1, girl_comb = fact[girls] / (actors - 4);
    for (int i = 0; i < 4; i++){
        boy_comb *= boys - i;
    }
    boy_comb /= 4;
    int girl_move = min(actors - 4, girls - (actors - 4));
    for (int i = 0; i < girl_move; i++){
        girl_comb *= girls - i;
    }
    girl_comb /= girl_move;
    // for (int b = 4; b <= min(boys, actors - 1); b++){
    //     ways += boy_comb * girl_comb;
    //     boy_comb = (boy_comb * (boys - b)) * (b / (b + 1));
    //     girl_comb = (girl_move / (girls - girl_move)) * ((girl_move) / (girl_move - 1));
    // }
    cout << ways << endl;
    return 0;
}