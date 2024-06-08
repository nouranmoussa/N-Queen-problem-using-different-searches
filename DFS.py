def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queen_using_dfs(board, col, n):
    #means all queens are placed
    if col >= n:
        return True
    
#iterates over rows
    for i in range(n):
        #if safe, place a queen
        if is_safe(board, i, col, n):
            board[i][col] = 1
            #recursive call for the next column
            if solve_n_queen_using_dfs(board, col + 1, n):
                return True
            #if no solution is found, backtracks by setting current position to 0
            board[i][col] = 0
    #If no safe position is found in the current column, needs further backtracking
    return False

def solve_n_queen(n):
    #intialize empty board
    board = [[0]*n for _ in range(n)]
    #empty list to store solution
    solutions = []

    #if no solution, return none
    if not solve_n_queen_using_dfs(board, 0, n):
        print("Solution does not exist")
        return None

    #if there's a solution, append it to the list
    solutions.append(board)
    return solutions

# Driver Code
solutions = solve_n_queen(5)
for i, solution in enumerate(solutions):
    print("Solution:")
    for row in solution:
        print(row)
    print()