float pierwiastek(float liczba)
{
    float dokladnosc = 0.000001;
    float a = liczba/2;

    while(modul(a-liczba/a) > dokladnosc)
    {
      a = (a+liczba/a)/2;
      if(a*a==liczba){
          break;
      }
    }

    return a;
}
