import numpy as np
from queue import PriorityQueue

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
    """Calculate the number of misplaced tiles."""
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
    def __init__(self, matrix, heuristic_score, g_score, parent=None):
        self.matrix = matrix
        self.heuristic_score = heuristic_score
        self.g_score = g_score
        self.parent = parent

    def __lt__(self, other):
        f_score = self.g_score + self.heuristic_score
        other_f_score = other.g_score + other.heuristic_score
        return f_score < other_f_score

def a_star_search(initial, goal):
    open_list = PriorityQueue()
    initial_state = PuzzleState(initial, heuristic(initial, goal), 0)  # g_score starts at 0
    open_list.put(initial_state)
    visited = {}  # Use a dictionary to track visited states and their g-scores
    visited[tuple(map(tuple, initial))] = 0

    while not open_list.empty():
        current_state = open_list.get()
        current_matrix = current_state.matrix

        if np.array_equal(current_matrix, goal):
            print("Goal state reached!")
            print_solution_path(current_state)
            return True

        for successor in generate_successors(current_matrix):
            successor_tuple = tuple(map(tuple, successor))
            new_g_score = current_state.g_score + 1  # Cost of moving is generally 1

            if successor_tuple not in visited or new_g_score < visited[successor_tuple]:
                visited[successor_tuple] = new_g_score
                successor_state = PuzzleState(successor, heuristic(successor, goal), new_g_score, current_state)
                open_list.put(successor_state)

    return False

def print_solution_path(state):
    path = []
    while state:
        path.append(state.matrix)
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
    if a_star_search(initial, goal):
        print("Solution found.")
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
