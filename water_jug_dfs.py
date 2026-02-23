import math

def dfs_with_path(a, b, target):
    
    # Solvability check
    if target > max(a, b) or target % math.gcd(a, b) != 0:
        return None
    
    stack = []
    visited = set()
    parent = {}
    
    start = (0, 0)
    stack.append(start)
    parent[start] = None
    
    while stack:
        x, y = stack.pop()   # LIFO
        
        if (x, y) in visited:
            continue
        
        visited.add((x, y))
        
        # Goal check
        if x == target or y == target:
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
        
        # Push neighbors
        for state in neighbors:
            if state not in visited:
                parent[state] = (x, y)
                stack.append(state)
    
    return None


a = int(input())
b = int(input())
target = int(input())

result = dfs_with_path(a, b, target)

if result:
    for step in result:
        print(step)
else:
    print("No solution")
