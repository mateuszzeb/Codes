#include <cstdlib>
#include <math.h>
#include <fstream>
#include <iostream>
#include <time.h>

using namespace std;

int main()
{
    ofstream plik("punkty.xls");
    float pi = 3.14159;
    float x;float y;float s; float alfa; 
    x=0;
    y=0;
    srand(time(NULL));
    for(int i=0;i<100;i++)
    {
        plik << x << "\t" << y << "\n";
        alfa = (float)rand() / RAND_MAX* (pi * 2);
        x += cos(alfa);
        y += sin(alfa);
    }
    plik.close();
}
