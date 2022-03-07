void bubble_sort(int *tab, int n){
    int temp;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n - i - 1; j++) {
            if (tab[j + 1] < tab[j]) {
                temp = tab[j];
                tab[j] = tab[j+1];
                tab[j+1] = temp;
            }
        }
    }
}
