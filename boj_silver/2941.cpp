#include <stdio.h>
#include <iostream>

using namespace std;

int main() {
    string latter;
    cin >> latter;
    string crolatter[8] = {"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="};

    for (auto lat : crolatter) {
        while(latter.find(lat) != string::npos){
            latter.replace(latter.find(lat),lat.size(), "a");
        }
    }
    cout << latter.size(); 
}
