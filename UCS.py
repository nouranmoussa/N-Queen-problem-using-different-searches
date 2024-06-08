from queue import PriorityQueue

def is_goal(state):
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            if state[i][j] == state[j][i] == 1:
                return False
    return True

def heuristic(state):
    #intializes the value of n, h
    n = len(state)
    h = 0
    for i in range(n):
        for j in range(i + 1, n):
            if state[i][j] == state[j][i] == 1:
                #incrementing the heuristic value for each pair of threatening queens found
                h += 1
    #returns the calculated heuristic value
    return h

def reconstruct_path(came_from, current):
    #This line initializes a list path with the current state as its only element
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1]

def solve_n_queen_ucs(n):
    #intializing
    start = [[0]*n for _ in range(n)]
    #initialize a priority queue
    frontier = PriorityQueue()
    #enqueue the start state with a priority of 0 and cost of 0
    frontier.put((0, 0, start))
    #empty dictionary to keep track of parents states
    came_from = {}
    #continues until the priority queue is empty
    while not frontier.empty():
        #retrieve and unpack the values from the front of the priority queue
        priority, cost, state = frontier.get()
        if is_goal(state):
            #If the state is a goal, it returns the reconstructed path from the start state to the goal state
            return reconstruct_path(came_from, state)
        for i in range(n):
            for j in range(n):
                #placing a queen in the unoccupied position
                if state[i][j] == 0:
                    new_state = [row[:] for row in state]
                    new_state[i][j] = 1
                    frontier.put((cost + heuristic(new_state), i, j, new_state))
                    came_from[new_state] = state
    return None

# Driver Code
solution = solve_n_queen_ucs(4)
if solution is not None:
    print("Solution:")
    for state in solution:
        print(state)
        print()
else:
    print("No solution found.")