import numpy as np

row, column = 3, 3

def input_func():
    print("Enter the entries rowwise (e.g., 1 2 3 for the first row):")
    matrix = []
    for _ in range(row):
        a = list(map(int, input().split()))
        matrix.append(a)
    return matrix

def printer(matrix_name):
    for i in range(row):
        for j in range(column):
            print(matrix_name[i][j], end=" ")
        print()

def heuristic(initial, goal):
   
    value = np.sum(initial != goal) - 1  # Subtract 1 to exclude the blank tile from the count
    return value

def swap_and_clone(matrix, x1, y1, x2, y2):
    new_matrix = np.copy(matrix)
    new_matrix[x1, y1], new_matrix[x2, y2] = new_matrix[x2, y2], new_matrix[x1, y1]
    return new_matrix

def generate_successors(matrix_name1):
    successors = []
    x, y = np.where(matrix_name1 == 0)[0][0], np.where(matrix_name1 == 0)[1][0]

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    for dx, dy in moves:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < row and 0 <= new_y < column:
            child_matrix = swap_and_clone(matrix_name1, x, y, new_x, new_y)
            successors.append(child_matrix)
    return successors
class PuzzleState:
    def __init__(self, matrix, heuristic_score, parent=None):
        self.matrix = matrix
        self.heuristic_score = heuristic_score
        self.parent = parent

    def __lt__(self, other):
        return self.heuristic_score < other.heuristic_score

def hill_climbing_search(initial, goal):
    current_state = PuzzleState(initial, heuristic(initial, goal))
    visited = set()
    visited.add(tuple(map(tuple, initial)))

    while True:
        current_matrix = current_state.matrix
        current_heuristic = current_state.heuristic_score

        if np.array_equal(current_matrix, goal):
            print("Goal state reached!")
            print_solution_path(current_state)
            return True

        successors = generate_successors(current_matrix)
        next_state = None
        for successor in successors:
            successor_tuple = tuple(map(tuple, successor))
            if successor_tuple not in visited:
                visited.add(successor_tuple)
                successor_heuristic = heuristic(successor, goal)
                if next_state is None or successor_heuristic < next_state.heuristic_score:
                    next_state = PuzzleState(successor, successor_heuristic, current_state)

        if next_state is None or next_state.heuristic_score >= current_heuristic:
            print("No more improvements possible.")
            return False

        current_state = next_state

def print_solution_path(state):
    path = []
    while state:
        path.append(state.matrix)  # Store the matrix of the state
        state = state.parent

    path.reverse()  # From initial to goal

    for step, matrix in enumerate(path):
        print(f"Step {step}:")
        printer(matrix)
        print()


def main():
    initial = np.array(input_func())
    goal = np.array(input_func())
    print("Initial State:")
    printer(initial)
    print("Goal State:")
    printer(goal)
    if hill_climbing_search(initial, goal):
        print("Solution found.")
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
