def NQueenSolver(N):
    def is_safe(board, row, col):
        for i in range(col):
            if board[row][i] == 1:
                return False
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        for i, j in zip(range(row, N, 1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        return True

    def solve(board, col):
        N = len(board)
        if col >= N:
            return True
        for i in range(N):
            if is_safe(board, i, col):
                board[i][col] = 1
                if solve(board, col + 1):
                    return True
                board[i][col] = 0
        return False

    board = [[0 for _ in range(N)] for _ in range(N)]
    if not solve(board, 0):
        return []
    return board

#Driver Code
solution = NQueenSolver(5)
print("Solution:")
for row in solution:
    print(row)