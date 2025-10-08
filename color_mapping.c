#include <stdio.h>
#include <stdbool.h>

#define V 4

void printSolution(int color[]);
bool isSafe(int v, int graph[V][V], int color[], int c);
bool graphColoringUtil(int graph[V][V], int m, int color[], int v);
bool graphColoring(int graph[V][V], int m);

void printSolution(int color[]) {
    printf("Solution Exists: The assigned colors are:\n");
    for (int i = 0; i < V; i++)
        printf("Vertex %d -> Color %d\n", i, color[i]);
    printf("\n");
}

/* A utility function to check if the current color assignment is safe for vertex v.
   It checks if there is any adjacent vertex of v that is already colored with color c. */
bool isSafe(int v, int graph[V][V], int color[], int c) {
    for (int i = 0; i < V; i++) {
        // Check if there is an edge AND the adjacent vertex 'i' has the same color 'c'
        if (graph[v][i] && c == color[i])
            return false;
    }
    return true;
}

/* A recursive utility function to solve the M-Coloring problem */
bool graphColoringUtil(int graph[V][V], int m, int color[], int v) {
    // Base Case: If all vertices are processed, a solution is found
    if (v == V) {
        printSolution(color);
        return true; // Return true to stop and print the first solution
        // To find all solutions, you would replace 'return true;' with 'return false;'
        // to force backtracking and keep exploring other options.
    }

    // Try all colors from 1 to m for the current vertex v
    for (int c = 1; c <= m; c++) {
        // Check if color c can be assigned to v
        if (isSafe(v, graph, color, c)) {
            // Assign the color
            color[v] = c;

            // Recurse for the next vertex (v + 1)
            if (graphColoringUtil(graph, m, color, v + 1))
                return true;

            // Backtrack: If assigning color c doesn't lead to a solution,
            // unassign it and try the next color.
            color[v] = 0;
        }
    }

    // If no color can be assigned to this vertex, return false
    return false;
}

/* The main function to solve M-Coloring problem */
bool graphColoring(int graph[V][V], int m) {
    // Initialize all vertices as uncolored (color 0)
    int color[V];
    for (int i = 0; i < V; i++)
        color[i] = 0;

    // Call the recursive utility function for vertex 0
    if (graphColoringUtil(graph, m, color, 0) == false) {
        printf("Solution does not exist with %d colors.\n", m);
        return false;
    }

    return true;
}

// Driver code
int main() {
    /* Create a sample graph (Adjacency Matrix Representation)
       The graph is:
        (0)---(1)
         | \ / |
         | / \ |
        (2)---(3)
        Edges: (0,1), (0,2), (0,3), (1,2), (1,3), (2,3) -> This is a complete graph K4.
        It requires 4 colors, but let's try with m=3 first.
    */
    int graph[V][V] = {
        {0, 1, 1, 1},
        {1, 0, 1, 1},
        {1, 1, 0, 1},
        {1, 1, 1, 0},
    };

    // Maximum number of colors available (m)
    int m = 3; 

    printf("Attempting to color the graph with %d colors:\n", m);
    graphColoring(graph, m);

    // Now try with the required 4 colors (Chromatic Number is 4 for K4)
    m = 4;
    printf("\nAttempting to color the graph with %d colors:\n", m);
    graphColoring(graph, m);

    return 0;
}