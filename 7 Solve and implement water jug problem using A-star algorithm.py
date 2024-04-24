import heapq

def heuristic(current_x, current_y, goal_x, goal_y):
   
    dx = abs(current_x - goal_x) if goal_x != -1 else 0
    dy = abs(current_y - goal_y) if goal_y != -1 else 0
    return dx + dy

def a_star(capacity_x, capacity_y, goal_x, goal_y):
    priority_queue = []  
    heapq.heappush(priority_queue, (0, (0, 0), None))  # (priority, state, parent)
    visited = set()
    parent_of = {(0, 0): None}

    while priority_queue:
        f, (current_x, current_y), parent = heapq.heappop(priority_queue)

        if (current_x, current_y) in visited:
            continue  

        visited.add((current_x, current_y))
        parent_of[(current_x, current_y)] = parent

        if (goal_x == -1 or current_x == goal_x) and (goal_y == -1 or current_y == goal_y):
            path = [(current_x, current_y)]
            while parent_of[(current_x, current_y)] is not None:
                current_x, current_y = parent_of[(current_x, current_y)]
                path.append((current_x, current_y))
            return path[::-1]

        states = [
            (capacity_x, current_y),  
            (current_x, capacity_y), 
            (0, current_y),  
            (current_x, 0),  
            ((current_x - min(current_x, capacity_y - current_y)), current_y + min(current_x, capacity_y - current_y)),
            (current_x + min(current_y, capacity_x - current_x), (current_y - min(current_y, capacity_x - current_x))), 
        ]

        for new_x, new_y in states:
            if (new_x, new_y) not in visited:
                g = f - heuristic(current_x, current_y, goal_x, goal_y) + 1
                h = heuristic(new_x, new_y, goal_x, goal_y)  
                new_f = g + h                          
                heapq.heappush(priority_queue, (new_f, (new_x, new_y), (current_x, current_y)))

    return None  

def main():
    capacity_x, capacity_y = map(int, input("Enter the capacities of the two jugs : ").split())
    goal_x, goal_y = map(int, input("Enter the goal amount for each jug (use -1 for no specific goal) : ").split())

    path = a_star(capacity_x, capacity_y, goal_x, goal_y)
    if path:
        print("Path to reach the goal:")
        for step in path:
            print(step)
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
