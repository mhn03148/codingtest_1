#include<stdio.h>
#include <iostream>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;
    int baguni[a];
    fill_n(baguni,a,0);
    
    for (int c=0; c<b; c++) {
        int i,j,k;
        cin >> i >> j >> k;
        for (int s = i-1; s<j; s++) {
            baguni[s] = k;
        } 
    }
    for (auto o : baguni){
        cout << o << " ";
    }  
}
