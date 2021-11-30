#include <cstdlib>
#include <iostream>
#include <time.h>
#include <fstream>

using namespace std;

float f(float x){
    return x * x + 1;
}

float modul(float a){
    if(a < 0) return -a;
    return a;
}

float pole_trapezu(float a, float b){
    float x;
    float y;
    int pkt = 0;
    for(int i = 0; i < 35000; i++){
        x = (float)rand() / RAND_MAX * (b - a) + a;
        y = (float)rand() / RAND_MAX * f(b);
        if(y <= f(x)){
            pkt++;
        }
    }
    return modul(b-a) * f(b) * (pkt / (float)35000);
}

int main()
{
    cout << pole_trapezu(1, 3);
    return 0;
}
