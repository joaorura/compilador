void shellSort(int[]* vet)
{
    int i, j, value;
    int size = len(&vet);
    int h = 1;
    
    while (h < size) {
        h = 3 * h + 1;
    }

    while (h > 0) {
        for(i : (h, size, 1) {
            value = vet[i];
            j = i;
            while (j > h-1 && value <= vet[j - h]) {
                vet[j] = vet[j - h];
                j = j - h;
            }
            vet[j] = value;
        }
        h = h/3;
    }
}

int main()
{
    int size;
    scan(size)

    int[size] array;

    for(int i : (0, size, 1)) {
        scan(array[i])
    }

    for(int i : (0, size, 1)) {
        print(array[i])
    }
    
    shellSort(&array);

    for(int i : (0, size, 1)) {
        print("%i", array[i])
    }

    return 0;
}