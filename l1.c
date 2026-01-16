#include<stdio.h>

#define MAX 10

int my_abs(int x)
{
    if(x < 0)
        return -x;
    return x;
}

int main()
{
    int row1, col1, row2, col2;
    int i, j, k;
    int is_eligible, row2_updated, col1_updated;
    int result[MAX][MAX];

    // initialize result
    for(i=0;i<MAX;i++)
        for(j=0;j<MAX;j++)
            result[i][j] = 0;

    printf("Enter the size of row1:- ");
    scanf("%d",&row1);
    printf("Enter the size of col1:- ");
    scanf("%d",&col1);

    int matrix1[row1][col1];

    printf("Enter the size of row2:- ");
    scanf("%d",&row2);
    printf("Enter the size of col2:- ");
    scanf("%d",&col2);

    int matrix2[row2][col2];

    row2_updated = row2;
    col1_updated = col1;

    printf("Enter elements for Matrix 1\n");
    for(i=0;i<row1;i++)
        for(j=0;j<col1;j++)
            scanf("%d",&matrix1[i][j]);

    printf("Enter elements for Matrix 2\n");
    for(i=0;i<row2;i++)
        for(j=0;j<col2;j++)
            scanf("%d",&matrix2[i][j]);

    if(col1 != row2)
    {
        is_eligible = my_abs(col1 - row2);

        if(col1 > row2)
            row2_updated = row2 + is_eligible;
        else
            col1_updated = col1 + is_eligible;
    }

    // Case 1: expand matrix1
    if(col1_updated != col1)
    {
        printf("\nColumn of Matrix 1 updated...\n");

        int matrix1_updated[row1][col1_updated];

        for(i=0;i<row1;i++)
            for(j=0;j<col1;j++)
                matrix1_updated[i][j] = matrix1[i][j];

        for(i=0;i<row1;i++)
            for(j=col1;j<col1_updated;j++)
            {
                printf("Enter element matrix1[%d][%d]: ",i,j);
                scanf("%d",&matrix1_updated[i][j]);
            }

        printf("\nUpdated Matrix 1\n");
        for(i=0;i<row1;i++)
        {
            for(j=0;j<col1_updated;j++)
                printf("%d ",matrix1_updated[i][j]);
            printf("\n");
        }

        for(i=0;i<row1;i++)
            for(j=0;j<col2;j++)
                for(k=0;k<col1_updated;k++)
                    result[i][j] += matrix1_updated[i][k] * matrix2[k][j];
    }

    // Case 2: expand matrix2
    else if(row2_updated != row2)
    {
        printf("\nRow of Matrix 2 updated...\n");

        int matrix2_updated[row2_updated][col2];

        for(i=0;i<row2;i++)
            for(j=0;j<col2;j++)
                matrix2_updated[i][j] = matrix2[i][j];

        for(i=row2;i<row2_updated;i++)
            for(j=0;j<col2;j++)
            {
                printf("Enter element matrix2[%d][%d]: ",i,j);
                scanf("%d",&matrix2_updated[i][j]);
            }

        printf("\nUpdated Matrix 2\n");
        for(i=0;i<row2_updated;i++)
        {
            for(j=0;j<col2;j++)
                printf("%d ",matrix2_updated[i][j]);
            printf("\n");
        }

        for(i=0;i<row1;i++)
            for(j=0;j<col2;j++)
                for(k=0;k<row2_updated;k++)
                    result[i][j] += matrix1[i][k] * matrix2_updated[k][j];
    }

    // Case 3: normal multiply
    else
    {
        for(i=0;i<row1;i++)
            for(j=0;j<col2;j++)
                for(k=0;k<col1;k++)
                    result[i][j] += matrix1[i][k] * matrix2[k][j];
    }

    printf("\nResult Matrix\n");
    for(i=0;i<row1;i++)
    {
        for(j=0;j<col2;j++)
            printf("%d\t",result[i][j]);
        printf("\n");
    }

    return 0;
}
