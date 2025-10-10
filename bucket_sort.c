#include <stdio.h>
#include <stdlib.h>

#define N 10  
#define BUCKET_COUNT 10  

void insertionSort(float arr[], int n) {
    for (int i = 1; i < n; i++) {
        float key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

void bucketSort(float arr[], int n) {
 
    float buckets[BUCKET_COUNT][N];
    int bucketSize[BUCKET_COUNT] = {0};


    for (int i = 0; i < n; i++) {
        int index = (int)(arr[i] * BUCKET_COUNT); 
        buckets[index][bucketSize[index]++] = arr[i];
    }

    for (int i = 0; i < BUCKET_COUNT; i++) {
        if (bucketSize[i] > 0)
            insertionSort(buckets[i], bucketSize[i]);
    }

    int k = 0;
    for (int i = 0; i < BUCKET_COUNT; i++) {
        for (int j = 0; j < bucketSize[i]; j++) {
            arr[k++] = buckets[i][j];
        }
    }
}

int main() {
    float arr[N] = {0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68};

    printf("Original array:\n");
    for (int i = 0; i < N; i++)
        printf("%.2f ", arr[i]);
    printf("\n");

    bucketSort(arr, N);

    printf("\nSorted array:\n");
    for (int i = 0; i < N; i++)
        printf("%.2f ", arr[i]);
    printf("\n");

    return 0;
}
