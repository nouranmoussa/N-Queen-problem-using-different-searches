#Neighbors: the states that can be reached from a given state by making a single move.
#Parents: the states that precede a given state in the exploration process.

from heapq import heappush, heappop
from copy import deepcopy

class State:
    def __init__(self, board, n):
        self.board = board
        self.n = n
        #intializing
        self.heuristic = self.calculate_heuristic()
        #will be used to track the parent state during the search
        self.parent = None

    #computes the heuristic value by counting the number of conflicting queens on the board
    def calculate_heuristic(self):
        #intializing
        h = 0
        #iterate over rows
        for i in range(self.n):
            #iterate over cols
            for j in range(i + 1, self.n):
                #if there is a queen in the current pair of rows and columns
                if self.board[i][j] == 1:
                    #the absolute difference between the indices i and j
                    #measures how far apart the threatening queens are
                    h += abs(i - j)
        return h

    #ordering in the priority queue based on the heuristic value
    def __lt__(self, other):
        return self.heuristic < other.heuristic

    def get_neighbors(self):
        #to store neighbors states
        neighbors = []
        for i in range(self.n):
            for j in range(i + 1, self.n):
                #if there is a queen in the current pair of rows and columns
                if self.board[i][j] == 1:
                    #creates a deep copy of the current chessboard configuration
                    new_board = deepcopy(self.board)
                    #swaps the positions of two threatening queens in the deep-copied chessboard
                    new_board[i][j], new_board[j][i] = new_board[j][i], new_board[i][j]
                    #modification
                    neighbors.append(State(new_board, self.n))
        return neighbors

    def is_goal(self):
        #if the heuristic value is 0, indicating that no queens threaten each other
        return self.heuristic == 0

    def __str__(self):
        return '\n'.join([''.join(map(str, row)) for row in self.board])

def AstarSearch(initial_state):
    #open_set: Priority queue to store states yet to be explored.
    #closed_set: Set to store the IDs of states that have already been explored.
    open_set = []
    closed_set = set()
    #Adds the initial state to the priority queue based on its heuristic value.
    heappush(open_set, initial_state)

    while open_set:
        #Retrieves and removes the state with the lowest heuristic value from the priority queue.
        current_state = heappop(open_set)
        closed_set.add(id(current_state))

        if current_state.is_goal():
            return current_state

        for neighbor in current_state.get_neighbors():
            #Checks if the neighbor has not been explored before.
            if id(neighbor) not in closed_set:
                heappush(open_set, neighbor)

    return None

def solve(N):
    initial_board = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        initial_board[i][i] = 1

    initial_state = State(initial_board, N)
    solution = AstarSearch(initial_state)

    if solution is None:
        return "No solution found"

    states = []
    while solution:
        states.append(solution.board)
        solution = solution.parent
    #reverse to present the solution path from the initial state to the goal state    
    return states[::-1]

solution = solve(4)
for row in solution:
    print(row)