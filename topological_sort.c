#include <stdio.h>
#include <stdlib.h>

#define MAX 100

int adj[MAX][MAX];   
int visited[MAX];
int stack[MAX];
int top = -1;
int V;  


void push(int v) {
    stack[++top] = v;
}


void dfs(int v) {
    visited[v] = 1;
    for (int i = 0; i < V; i++) {
        if (adj[v][i] && !visited[i]) {
            dfs(i);
        }
    }
    push(v);  
}

void topologicalSort() {
    for (int i = 0; i < V; i++) {
        if (!visited[i]) {
            dfs(i);
        }
    }

    printf("Topological Sort: ");
    while (top != -1) {
        printf("%d ", stack[top--]);
    }
    printf("\n");
}


int main() {
    int E, u, v;

    printf("Enter number of vertices: ");
    scanf("%d", &V);

    printf("Enter number of edges: ");
    scanf("%d", &E);

    
    for (int i = 0; i < V; i++)
        for (int j = 0; j < V; j++)
            adj[i][j] = 0;

    printf("Enter edges (u v) for directed graph:\n");
    for (int i = 0; i < E; i++) {
        scanf("%d %d", &u, &v);
        adj[u][v] = 1;  
    }

    topologicalSort();
    return 0;
}
