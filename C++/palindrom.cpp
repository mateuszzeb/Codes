#include <iostream>

using namespace std;

string bez_spacji(string s){
    string n = "";
    for(int i = 0; i < s.length(); i++){
        if(s[i] != ' '){
            n+=s[i];
        }
    }
    return n;
}
string lower(string s){
    for(int i = 0; i < s.length(); i++){
        if(s[i] >= 'A' && s[i] <= 'Z'){
            s[i]-=32;
        }
    }
    return s;
}
bool czy_palindrom(string s){
    s = lower(bezspacji(s));
    for(int i = 0, j = s.length() - 1; i < j; i++, j--){
        if(s[i] != s[j]) return false;
    }
    return true;

}
int main()
{
    cout << czy_palindrom("ala");
    return 0;
}
