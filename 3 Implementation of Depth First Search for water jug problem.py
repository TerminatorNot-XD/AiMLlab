def dfs(capacity_x, capacity_y, goal_x, goal_y):
    stack = [(0, 0)]
    visited = set()
    visited.add((0,0))
    parent_of = {(0, 0): None}

    while stack:
        current_x, current_y = stack.pop()

        if (goal_x == -1 or current_x == goal_x) and (goal_y == -1 or current_y == goal_y):
            path = [(current_x, current_y)]
            while parent_of[(current_x, current_y)] is not None:
                current_x, current_y = parent_of[(current_x, current_y)]
                path.append((current_x, current_y))
            return path[::-1]

        # Generate and explore all possible next states
        states = [
            (capacity_x, current_y),  # Fill jug X
            (current_x, capacity_y),  # Fill jug Y
            (0, current_y),           # Empty jug X
            (current_x, 0),           # Empty jug Y
            ((current_x - min(current_x, capacity_y - current_y)), current_y + min(current_x, capacity_y - current_y)),  # Pour from X to Y
            (current_x + min(current_y, capacity_x - current_x), (current_y - min(current_y, capacity_x - current_x))),  # Pour from Y to X
        ]

        for new_x, new_y in states:
            if (new_x, new_y) not in visited:
                stack.append((new_x, new_y))
                visited.add((new_x, new_y))
                parent_of[(new_x, new_y)] = (current_x, current_y)

    return None

def main():
    capacity_x, capacity_y =  map(int, input("Enter the capacities of the two jugs : ").split())
    goal_x, goal_y =map(int, input("Enter the goal amount for each jug (use -1 for no specific goal) : ").split())

    path = dfs(capacity_x, capacity_y, goal_x, goal_y)
    if path:
        print("Path to reach the goal:")
        for step in path:
            print(step)
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
