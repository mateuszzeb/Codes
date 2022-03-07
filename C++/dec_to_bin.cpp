void dec_to_bin(int liczba)
{
    int i = 0;
    int tab[32];
    while(liczba > 0)
    {
        tab[i] = liczba % 2;
        liczba /= 2;
        i++;
    }
    for(int j = i - 1; j >= 0; j--){
        cout << tab[j];
    }
}
