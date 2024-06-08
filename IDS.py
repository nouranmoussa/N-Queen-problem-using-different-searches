def is_safe(board, row, col, n):
    for i in range(col):
        if board[i] == row or abs(board[i] - row) == abs(i - col):
            return False
    return True

def print_solution(board):
    for row in board:
        line = ["1" if i == row else "0" for i in range(len(board))]
        print(" ".join(line))

def solve_n_queens_ids(n):
    #depth represents the maximum depth of the search for a solution
    for depth in range(1, n+1):
        #intialize the board
        board = [-1] * n
        #calls the function with the current board configuration, starting column index 0
        if ids_util(board, 0, n, depth):
            #if a solutions if found
            return board
    #no solution    
    return None

def ids_util(board, col, n, depth):
    if col >= n:
        return True

    #checks if the maximum depth is exhausted/reached the specified maximum depth for exploration without finding a solution
    if depth <= 0:
        return False

    for row in range(n):
        if is_safe(board, row, col, n):
            #place a queen
            board[col] = row
            #recursive call for next move
            if ids_util(board, col + 1, n, depth - 1):
                return True
            board[col] = -1

    return False

if __name__ == "__main__":
    n = 5  
    solution = solve_n_queens_ids(n)

    if solution:
        print_solution(solution)
    else:
        print("No solution found.")
