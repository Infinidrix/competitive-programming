#include <bits/stdc++.h>

using namespace std;

int main(){
    while (true){
        int d, dep;
        long double pay, loan;
        cin >> d >> pay >> loan >> dep;
        if (d < 0){
            break;
        }
        // cout << d << pay << loan << dep;
        vector<pair<int, long double>> deps(dep);
        for (int i = 0; i < dep; i++){
            int tempMonth; 
            string tempPercent;
            cin >> tempMonth >> tempPercent;
            // scanf("%d%*c%*c%s", &tempMonth, tempPercent);
            // cout << tempMonth << tempPercent;
            long double percent = stold("0" + tempPercent);
            deps[i] = make_pair(tempMonth, percent);
        }
        long double carPay = loan * (1 - deps[0].second) + pay;
        long double monthlyPay = loan / d;
        int ind = 0;
        for (int i = 1; i <= 100; i++){
            if (ind < deps.size() - 1 && deps[ind + 1].first == i){
                ind++;
            }
            carPay *= (1 - deps[ind].second);
            loan -= monthlyPay;
            // cout << "month " << i << " interest " << (deps[ind].second) << endl; 
            // cout <<  "car pay " << carPay << " loan " << loan << '\n';
            if (loan < carPay){
                cout << i << " ";
                if (i == 1) {
                    cout << "month" << '\n';
                } else{
                    cout << "months" << '\n';
                }
                break;
            }
        }
    }
}