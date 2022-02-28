#include <iostream>
using namespace std;

int main(){
    int n, *tab;
    cout << "> ";
    cin >> n;
    tab = new int[n];
    for(int i = 0; i < n; i++) tab[i] = false;
    for(int i = 2; i * i < n; i++){
        if(!tab[i]){
            for(int j = i*i; j <= n; j+=i){
                tab[j] = true;
            }
        }
    }
    for(int i = 2; i < n; i++){
        if(!tab[i]){
            cout << i << " ";
        }
    }
    return 0;
}
