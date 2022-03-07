void insertion_sort(int *tab, int n){
    int i_min;
    int temp;
    for(int i = 0; i < n - 1; i++){
        i_min = i;
        for(int j = i + 1; j < n; j++){
            if(tab[j] < tab[i_min]){
                i_min = j;
            }
        }
        temp = tab[i];
        tab[i] = tab[i_min];
        tab[i_min] = temp;
    }
}
