float pi(){
    int ilosc_losowan = 100000000;
    int w_kole = 0;
    float x;
    float y;
    srand(time(NULL));
    for(int i = 0; i < ilosc_losowan; i++){
        x=(float)rand()/RAND_MAX;
        y=(float)rand()/RAND_MAX;
        if(x*x+y*y<=1) w_kole++;
    }
    float PI = 4 * w_kole / (float)ilosc_losowan;
    return PI;
}
