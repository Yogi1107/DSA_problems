#include <stdio.h>

#define MAX 20

int parent[MAX];

// Function to find the root of a set
int FIND(int i) {
    while (parent[i] >= 0)
        i = parent[i];
    return i;
}

// Function to union two sets
void UNION(int i, int j) {
    parent[i] = j;
}

// Function to adjust heap (min-heap)
void ADJUST(int cost[][MAX], int edges[][3], int m, int n) {
    int i, j, val, u, v;
    for (i = 1; i <= m / 2; i++) {
        j = i * 2;
        if (j < m && edges[j + 1][2] < edges[j][2])
            j++;
        if (edges[j][2] < edges[i][2]) {
            u = edges[i][0];
            v = edges[i][1];
            val = edges[i][2];
            edges[i][0] = edges[j][0];
            edges[i][1] = edges[j][1];
            edges[i][2] = edges[j][2];
            edges[j][0] = u;
            edges[j][1] = v;
            edges[j][2] = val;
        }
    }
}

// Heapify the edge list
void HEAPIFY(int edges[][3], int m) {
    int i;
    for (i = m / 2; i >= 1; i--) {
        ADJUST(NULL, edges, m, i);
    }
}

// Delete minimum cost edge
void DELETE_MIN(int edges[][3], int *m, int *u, int *v, int *w) {
    *u = edges[1][0];
    *v = edges[1][1];
    *w = edges[1][2];
    edges[1][0] = edges[*m][0];
    edges[1][1] = edges[*m][1];
    edges[1][2] = edges[*m][2];
    (*m)--;
    ADJUST(NULL, edges, *m, 1);
}

// Kruskal’s algorithm
void Kruskal(int edges[][3], int cost[][MAX], int n, int m) {
    int t[MAX][2], i, j, k, u, v, w;
    float mincost = 0.0;

    HEAPIFY(edges, m);

    for (i = 1; i <= n; i++)
        parent[i] = -1;

    i = 0;

    while (i < n - 1 && m > 0) {
        DELETE_MIN(edges, &m, &u, &v, &w);
        j = FIND(u);
        k = FIND(v);
        if (j != k) {
            i++;
            t[i][0] = u;
            t[i][1] = v;
            mincost += w;
            UNION(j, k);
        }
    }

    if (i != n - 1)
        printf("\nNo spanning tree exists.\n");
    else {
        printf("\nEdges in Minimum Spanning Tree:\n");
        for (j = 1; j <= i; j++)
            printf("%d -- %d\n", t[j][0], t[j][1]);
        printf("\nMinimum cost = %.2f\n", mincost);
    }
}

int main() {
    int n, m, i;
    int edges[MAX][3], cost[MAX][MAX];

    printf("Enter number of vertices: ");
    scanf("%d", &n);

    printf("Enter number of edges: ");
    scanf("%d", &m);

    printf("Enter edges (u v w):\n");
    for (i = 1; i <= m; i++) {
        scanf("%d %d %d", &edges[i][0], &edges[i][1], &edges[i][2]);
    }

    Kruskal(edges, cost, n, m);
    return 0;
}
