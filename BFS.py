from collections import deque

#check position
def is_safe(board, row, col, n):
    #Checks if there is a queen in the same row
    for i in range(col):
        if board[row][i] == 1:
            return False
    #Checks if there is a queen in the upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    #Checks if there is a queen in the lower-left diagonal
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    #If none of the above conditions are met, it's safe 
    return True

#n is size of the board 
def solve_n_queen_using_bfs(n):
    #intialize the board
    board = [[0]*n for _ in range(n)]
    #empty result set
    result = []
    #a queue with the initial state (empty board and column 0)
    queue = deque([(board, 0)])

    #Continues the BFS process as long as there are states in the queue. Dequeues the front of the queue
    while queue:
        temp_board, col = queue.popleft()

        #If the current column is equal to the size of the board, a solution is found, and it's appended to the result list
        if col == n:
            result.append(temp_board)
            continue

        #For each row in the current column, if it's safe to place a queen, it updates the board,
        #enqueues the new state with the updated board and the next column, and then resets the board to its previous state.
        for i in range(n):
            if is_safe(temp_board, i, col, n):
                temp_board[i][col] = 1
                queue.append(([row[:] for row in temp_board], col + 1))
                temp_board[i][col] = 0

    return result

# Driver Code
solutions = solve_n_queen_using_bfs(4)
for i, solution in enumerate(solutions):
    print(f"Solution {i+1}:")
    for row in solution:
        print(row)
    print()