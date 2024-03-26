#include <stdio.h>
#include <iostream>
#include <string>
using namespace std;
int main() {
    string latter, newlatter;
    cin >> latter;
    
    for (int i=0; i< latter.size(); i++) {
        newlatter += latter[latter.size()-i-1];
    }
    

    if (latter == newlatter) {
        cout << 1;
    } else {
        cout << 0;
    }
}
