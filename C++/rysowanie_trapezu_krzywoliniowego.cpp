#include <cstdlib>
#include <iostream>
#include <time.h>
#include <fstream>

using namespace std;
ofstream zapis("plik.xls");

float f(float x){
    return x * x + 1;
}
void rysowanie_trapezu(float a, float b){
    float x;
    float y;
    for(int i = 0; i < 35000; i++){
        x = (float)rand() / RAND_MAX * (b - a) + a;
        y = (float)rand() / RAND_MAX * f(b);
        if(y <= f(x)){
            zapis << x << "\t" << y << "\n";
        }
    }
}

int main()
{
    rysowanie_trapezu(1, 3);
    return 0;
}
