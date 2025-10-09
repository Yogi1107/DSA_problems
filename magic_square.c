#include <stdio.h>

int main() {
    int n, i, j, num;
    
    printf("Enter the size of magic square (odd number): ");
    scanf("%d", &n);

    if (n % 2 == 0) {
        printf("Magic square is not possible for even numbers!\n");
        return 0;
    }

    int magic[n][n];
  
    for (i = 0; i < n; i++)
        for (j = 0; j < n; j++)
            magic[i][j] = 0;

    i = 0;
    j = n / 2;
    for (num = 1; num <= n * n; ) {
        if (i < 0 && j == n) { 
            i += 2;
            j--;
        }
        else {
            if (i < 0)
                i = n - 1;
            if (j == n)
                j = 0;
        }

        if (magic[i][j]) { 
            i += 2;
            j--;
            continue;
        } else
            magic[i][j] = num++;

        i--;
        j++;
    }

    printf("\nThe Magic Square for n=%d:\n\n", n);
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++)
            printf("%4d", magic[i][j]);
        printf("\n");
    }

    return 0;
}
