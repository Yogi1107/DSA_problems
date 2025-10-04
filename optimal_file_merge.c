#include <stdio.h>

// Function to sort array in ascending order
void sort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

// Function to calculate OBMP
int optimalMerge(int files[], int n) {
    int totalCost = 0;

    // Keep merging until one file remains
    while (n > 1) {
        // Sort file sizes
        sort(files, n);

        // Take two smallest
        int first = files[0];
        int second = files[1];

        int cost = first + second;
        totalCost += cost;

        // Replace first two with their sum
        files[0] = cost;

        // Shift remaining files left
        for (int i = 1; i < n - 1; i++) {
            files[i] = files[i + 1];
        }
        n--;  // reduce size
    }

    return totalCost;
}

int main() {
    int n;
    printf("Enter number of files: ");
    scanf("%d", &n);

    int files[n];
    printf("Enter file sizes:\n");
    for (int i = 0; i < n; i++) {
        scanf("%d", &files[i]);
    }

    int result = optimalMerge(files, n);
    printf("Minimum total merge cost = %d\n", result);

    return 0;
}
