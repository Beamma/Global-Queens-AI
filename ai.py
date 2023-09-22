def n_queens_neighbours(state):
    
    neighbours = []
    for i in range(len(state)):
        for j in range(i+1, len(state)):
            state_list = list(state)
            state_list[i], state_list[j] = state_list[j], state_list[i]
            neighbours.append(tuple(state_list))


    return sorted(neighbours)

def n_queens_cost(state):
    cost = 0
    for i in range(len(state)):
        for j in range(i+1, len(state)):
            dx = i - j
            dy = state[i] - state[j]
            if abs(dx) == abs(dy):
                cost += 1
    
    return cost



def greedy_descent(initial_state, neighbours, cost):
    min_state = initial_state
    ans = [initial_state]
    current_min = cost(initial_state)
    min_cost = []
    while True:
        neighbours_states = neighbours(min_state)
        min_cost = []
        for state in neighbours_states:
            min_cost.append(cost(state))
        if len(min_cost) == 0:
            return ans

        if min(min_cost) >= current_min:
            return ans
        
        current_min = min(min_cost)
        min_state = neighbours_states[min_cost.index(current_min)]
        ans.append(min_state)


def greedy_descent_with_random_restart(random_state, neighbours, cost):
    state = random_state()

    states = greedy_descent(state,neighbours,cost)
    for s in states:
        print(s)
    min_cost = cost(states[-1])
    
    while min_cost > 0:
        print("RESTART")
        state = random_state()
        states = greedy_descent(state,neighbours,cost)
        for s in states:
            print(s)
        min_cost = cost(states[-1])
    

        


import random

N = 8
random.seed(0)

def random_state():
    return tuple(random.sample(range(1,N+1), N))   

greedy_descent_with_random_restart(random_state, n_queens_neighbours, n_queens_cost)

# X = (5, 8, 4, 1, 3, 6, 2, 7)
# print(n_queens_cost(X))