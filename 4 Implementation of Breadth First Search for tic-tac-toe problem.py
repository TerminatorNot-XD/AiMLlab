from collections import deque

class GameState:
    def __init__(self, board=None, current_player='X'):
        if board is None:
            self.board = [[' ' for _ in range(3)] for _ in range(3)]
        else:
            self.board = board
        self.current_player = current_player

    def is_win(self):
        # Check rows, columns, and diagonals for a win
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ' or \
           self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True
        return False

    def is_draw(self):
        for row in self.board:
            if ' ' in row:
                return False
        return not self.is_win()

    def get_possible_moves(self):
        moves = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    moves.append((i, j))
        return moves

    def apply_move(self, move):
        new_board = [row[:] for row in self.board]
        new_board[move[0]][move[1]] = self.current_player
        return GameState(new_board, 'O' if self.current_player == 'X' else 'X')

def find_best_move(game_state):
    queue = deque([(game_state, [])])  # Store states and moves made to reach them
    visited = set()  # Keep track of visited states

    while queue:
        state, moves_taken = queue.popleft()
        if state in visited:
            continue
        visited.add(state)

        if state.is_win(): 
            return moves_taken[0]  # Return the first move in the winning sequence

        for move in state.get_possible_moves():
            next_state = state.apply_move(move)
            queue.append((next_state, moves_taken + [move]))  

    return None  # No winning move found

def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 9)

def main():
    game_state = GameState()
    current_player = 'X'
    
    while True:
        print_board(game_state.board)
        if current_player == 'X':
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))
            except ValueError:
                print("Please enter numbers only.")
                continue
            if (row, col) in game_state.get_possible_moves():
                game_state = game_state.apply_move((row, col))
                if game_state.is_win():
                    print("You win!")
                    break
                elif game_state.is_draw():
                    print("It's a draw!")
                    break
                current_player = 'O'
            else:
                print("Invalid move, try again.")
        else:
            print("Computer's move:")
            move = find_best_move(game_state)
            if move:
                game_state = game_state.apply_move(move)
                print(f"Computer placed 'O' in position {move[0]}, {move[1]}.")
                if game_state.is_win():
                    print_board(game_state.board)
                    print("Computer wins!")
                    break
                elif game_state.is_draw():
                    print_board(game_state.board)
                    print("It's a draw!")
                    break
                current_player = 'X'
            else:
                print("No valid moves left!")
                break
    print_board(game_state.board)

if __name__ == "__main__":
    main()
