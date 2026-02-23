import heapq

# Goal state
GOAL = ((1,2,3),
        (4,5,6),
        (7,8,0))


# Manhattan Distance Heuristic
def heuristic(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_x = (value - 1) // 3
                goal_y = (value - 1) % 3
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance


# Find blank position
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


# Generate neighbors
def get_neighbors(state):
    neighbors = []
    x, y = find_blank(state)
    
    directions = [(-1,0),(1,0),(0,-1),(0,1)]  # up, down, left, right
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [list(row) for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(tuple(tuple(row) for row in new_state))
    
    return neighbors


# A* Algorithm
def a_star(start):
    open_list = []
    heapq.heappush(open_list, (0 + heuristic(start), 0, start))
    
    came_from = {}
    g_score = {start: 0}
    
    while open_list:
        f, g, current = heapq.heappop(open_list)
        
        if current == GOAL:
            return reconstruct_path(came_from, current)
        
        for neighbor in get_neighbors(current):
            tentative_g = g + 1
            
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic(neighbor)
                heapq.heappush(open_list, (f_score, tentative_g, neighbor))
                came_from[neighbor] = current
    
    return None


def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path


# --------------------
# INPUT
# --------------------
start = (
    (1,2,3),
    (4,0,6),
    (7,5,8)
)

solution = a_star(start)

if solution:
    print("Steps:", len(solution)-1)
    for step in solution:
        for row in step:
            print(row)
        print()
else:
    print("No solution")
