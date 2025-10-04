#include <stdio.h>
#include <limits.h>

// Function for Matrix Chain Multiplication
void matrixChainOrder(int p[], int n) {
    int m[n][n];   // cost table
    int s[n][n];   // split table

    // cost of one matrix is zero
    for (int i = 1; i < n; i++)
        m[i][i] = 0;

    // L = chain length
    for (int L = 2; L < n; L++) {
        for (int i = 1; i < n - L + 1; i++) {
            int j = i + L - 1;
            m[i][j] = INT_MAX;

            for (int k = i; k <= j - 1; k++) {
                int q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j];
                if (q < m[i][j]) {
                    m[i][j] = q;
                    s[i][j] = k;
                }
            }
        }
    }

    printf("Minimum number of multiplications = %d\n", m[1][n-1]);
}

// Driver code
int main() {
    int n;
    printf("Enter number of matrices: ");
    scanf("%d", &n);

    int p[n+1];
    printf("Enter dimensions (array of length %d):\n", n+1);
    for (int i = 0; i <= n; i++)
        scanf("%d", &p[i]);

    matrixChainOrder(p, n+1);

    return 0;
}
