#include <stdio.h>
#include <string>
#include <iostream>
using namespace std;

int main() {
    int N;
    cin >> N;
    
    string word;
    int ans = N;
    for (int i = 0; i < N; i++) {
        cin >> word;
        for (int i = 0; i<word.size()-1; i++) {
            if (word[i] == word[i+1]) {
                continue;
            } else {
                if (word.substr(i+1).find(word[i]) == string::npos) {
                    continue;
                } else {
                    ans--;
                    break;
                }
            }
        }
    }
    cout << ans;
}
