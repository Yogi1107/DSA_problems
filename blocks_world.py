import copy

# Goal configuration
GOAL = ['C', 'B', 'A']


def heuristic(state):
    """
    Count correctly placed blocks in correct order in first stack
    """
    if not state:
        return 0
    
    score = 0
    for stack in state:
        for i in range(min(len(stack), len(GOAL))):
            if stack[i] == GOAL[i]:
                score += 1
            else:
                break
    return score


def generate_neighbors(state):
    neighbors = []
    
    for i in range(len(state)):
        if not state[i]:
            continue
        
        for j in range(len(state)):
            if i == j:
                continue
            
            new_state = copy.deepcopy(state)
            
            block = new_state[i].pop()
            new_state[j].append(block)
            
            neighbors.append(new_state)
        
        # Move to new stack
        new_state = copy.deepcopy(state)
        block = new_state[i].pop()
        new_state.append([block])
        neighbors.append(new_state)
    
    return neighbors

def simple_hill_climbing(initial):
    current = initial
    
    while True:
        current_score = heuristic(current)
        neighbors = generate_neighbors(current)
        
        found_better = False
        
        for n in neighbors:
            if heuristic(n) > current_score:
                current = n
                found_better = True
                break
        
        if not found_better:
            return current


def steepest_ascent(initial):
    current = initial
    
    while True:
        current_score = heuristic(current)
        neighbors = generate_neighbors(current)
        
        best = current
        best_score = current_score
        
        for n in neighbors:
            score = heuristic(n)
            if score > best_score:
                best = n
                best_score = score
        
        if best_score <= current_score:
            return current
        
        current = best


initial_state = [['A'], ['B'], ['C']]

print("Initial:", initial_state)

result_simple = simple_hill_climbing(initial_state)
print("Simple Hill Climbing Result:", result_simple)

result_steepest = steepest_ascent(initial_state)
print("Steepest Ascent Result:", result_steepest)
