import math
from collections import deque

def bfs_with_path(a, b, target):
    
    # Solvability check
    if target > max(a, b) or target % math.gcd(a, b) != 0:
        return None
    
    queue = deque()
    visited = set()
    parent = {}
    
    start = (0, 0)
    queue.append(start)
    visited.add(start)
    parent[start] = None
    
    while queue:
        x, y = queue.popleft()
        
        # Goal check
        if x == target or y == target:
            # Reconstruct path
            path = []
            curr = (x, y)
            
            while curr is not None:
                path.append(curr)
                curr = parent[curr]
            
            path.reverse()
            return path
        
        # Generate neighbors
        neighbors = []
        
        # Fill A
        neighbors.append((a, y))
        
        # Fill B
        neighbors.append((x, b))
        
        # Empty A
        neighbors.append((0, y))
        
        # Empty B
        neighbors.append((x, 0))
        
        # Pour A -> B
        transfer = min(x, b - y)
        neighbors.append((x - transfer, y + transfer))
        
        # Pour B -> A
        transfer = min(y, a - x)
        neighbors.append((x + transfer, y - transfer))
        
        # Process neighbors
        for state in neighbors:
            if state not in visited:
                visited.add(state)
                parent[state] = (x, y)
                queue.append(state)
    
    return None


a = int(input())
b = int(input())
target = int(input())

result = bfs_with_path(a, b, target)

if result:
    for step in result:
        print(step)
else:
    print("No solution")
