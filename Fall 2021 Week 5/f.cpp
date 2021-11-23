#include <bits/stdc++.h>

using namespace std;

int main(){
    long long n, m;
    cin >> n >> m;
    auto comp = [](pair<long long, long long>& first, pair<long long, long long>& second){
        return first.first < second.first;
    };
    vector<long long> endInd(m + 1);
    vector<pair<long long, long long>> ends;
    vector<pair<long long, long long>> exams;
    vector<long long> days(m + 1);
    
    for (long long i = 0; i < n; i++){
        long long temp;
        cin >> temp;
        if (temp > 0){
            exams.push_back(make_pair(i, temp));
        }
        endInd[temp] = i;
    }
    for (long long i = 1; i < m + 1; i++){
        long long temp;
        cin >> temp;
        days[i] = temp;
    }
    // cout << "Days " << endl;
    // for (long long i = 0; i < days.size(); i++){
    //     cout << days[i] << " ";
    // }
    // cout << endl;
    for (long long i = 1; i < endInd.size(); i++){
        ends.push_back(make_pair(endInd[i], i));
    }
    sort(ends.begin(), ends.end(), comp);
    sort(exams.begin(), exams.end(), comp);
    vector<long long> visited(m + 1, false);
    long long additional = 0, prev = -1, j = 0, visited_count = 0;
    for(long long i = 0; i < ends.size(); i++){
        auto curr = ends[i];
        // cout << "On " << curr.first << " with index " << curr.second << endl;
        if (visited[curr.second]){
            continue;
        }
        if (days[curr.second] > curr.first - prev + additional - 1){
            cout << "-1" << endl;
            break;
        }
        additional = curr.first - prev + additional - 1;
        prev = curr.first;
        visited[curr.second] = true;
        visited_count++;
        additional -= days[curr.second];
        while (j < exams.size() && exams[j].first < prev){
            if (visited[exams[j].second] || days[exams[j].second] >= additional){
                j++;
            } else {
                // cout << "Got some for " << exams[j].second << " with additional " << additional <<endl;
                additional -= days[exams[j].second] + 1;
                visited[exams[j].second] = true;
                visited_count++;
            }
        }
        if (visited_count == m){
            cout << prev + 1 << endl;
            break;
        }
    }

}