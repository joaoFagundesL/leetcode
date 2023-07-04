void reverseString(char* s, int sSize){
    int i = 0;
    int j = sSize - 1;
    char aux;

    // <= because there is a case where i = j does not happen
    while(i <= j) {
        aux = s[j];
        s[j] = s[i];
        s[i] = aux;
        j--;
        i++;
    }
}
