#include <stdio.h>

double power(double base, int exponent) {
    if (exponent == 0) {
        return 1;
    }

    double result = power(base, exponent / 2);
    result *= result;

    if (exponent % 2 != 0) {
        result *= base;
    }

    return result;
}

int main() {
    double base;
    int exponent;

    printf("Enter the base: ");
    scanf("%lf", &base);

    printf("Enter the exponent: ");
    scanf("%d", &exponent);

    double result = power(base, exponent);
    printf("%lf^%d = %lf\n", base, exponent, result);

    return 0;
}