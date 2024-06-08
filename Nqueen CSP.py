def is_safe(board, row, col, N):
    # Check if there is a queen in the same row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check if there is a queen in the upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check if there is a queen in the lower diagonal on the left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens_util(board, col, N):
    # Base case: all queens are placed
    if col >= N:
        return True

    # Creates a list of row indices sorted by the number of queens already placed in each row
    # Prioritize rows with fewer conflicts
    sorted_rows = sorted(range(N), key=lambda row: sum(board[row]))

    for i in sorted_rows:
        if is_safe(board, i, col, N):
            board[i][col] = 1

            if solve_nqueens_util(board, col + 1, N):
                return True
            # backtrack by resetting the current position
            board[i][col] = 0

    return False

def solve_nqueens(N):
    # Initialize the chessboard
    board = [[0] * N for _ in range(N)]

    if not solve_nqueens_util(board, 0, N):
        print("No solution exists.")
        return None

    return board

def print_board(board):
    for row in board:
        line = ""
        for cell in row:
            line += "1 " if cell == 1 else "0 "
        print(line)

# Set the size of the chessboard
N = 5

# Solve the N-Queens problem using backtracking with ordering
final_state = solve_nqueens(N)

# Print the solution
if final_state:
    print("Initial State:")
    print_board([[0] * N for _ in range(N)])

    print("\nFinal State:")
    print_board(final_state)
