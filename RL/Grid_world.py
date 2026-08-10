import random
import numpy as np


ROWS = 3
COLS = 4

START = (2, 0)

GOAL = (0, 3)
TRAP = (1, 3)

WALL = (1, 1)

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

LEAVING_REWARD = -0.0

state_dict = {
    (0,0):0,
    (0,1):1,
    (0,2):2,
    (0,3):3,

    (1,0):4,
    (1,2):5,
    (1,3):6,

    (2,0):7,
    (2,1):8,
    (2,2):9,
    (2,3):10,
}

def get_state(agent):
    return state_dict[agent]

reverse_state = {}

for position, state in state_dict.items():
    reverse_state[state] = position



def reset():
    return START


def step(agent, action , leaving_reward):

    row, col = agent

    new_row = row
    new_col = col


    if action == UP:
        new_row -= 1

    elif action == RIGHT:
        new_col += 1

    elif action == DOWN:
        new_row += 1

    elif action == LEFT:
        new_col -= 1


    if new_row < 0 or new_row >= ROWS:
        new_row = row

    if new_col < 0 or new_col >= COLS:
        new_col = col


    if (new_row, new_col) == WALL:
        new_row = row
        new_col = col

    agent = (new_row, new_col)


    reward = leaving_reward
    done = False

    if agent == GOAL:
        reward = 1
        done = True

    elif agent == TRAP:
        reward = -1
        done = True
    
    
    return agent, reward, done



def render(agent):

    print()

    for r in range(ROWS):

        for c in range(COLS):

            if (r, c) == agent:
                text = " A "

            elif (r, c) == START:
                text = " S "

            elif (r, c) == GOAL:
                text = "+1 "

            elif (r, c) == TRAP:
                text = "-1 "

            elif (r, c) == WALL:
                text = "XXX"

            else:
                text = "   "

            print(f"|{text}", end="")

        print("|")

        print("+---"*COLS + "+")


import random
import numpy as np


ROWS = 3
COLS = 4

START = (2, 0)

GOAL = (0, 3)
TRAP = (1, 3)

WALL = (1, 1)

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

LEAVING_REWARD = -0.0

state_dict = {
    (0,0):0,
    (0,1):1,
    (0,2):2,
    (0,3):3,

    (1,0):4,
    (1,2):5,
    (1,3):6,

    (2,0):7,
    (2,1):8,
    (2,2):9,
    (2,3):10,
}

def get_state(agent):
    return state_dict[agent]

reverse_state = {}

for position, state in state_dict.items():
    reverse_state[state] = position



def reset():
    return START


def step(agent, action , leaving_reward):

    row, col = agent

    new_row = row
    new_col = col


    if action == UP:
        new_row -= 1

    elif action == RIGHT:
        new_col += 1

    elif action == DOWN:
        new_row += 1

    elif action == LEFT:
        new_col -= 1


    if new_row < 0 or new_row >= ROWS:
        new_row = row

    if new_col < 0 or new_col >= COLS:
        new_col = col


    if (new_row, new_col) == WALL:
        new_row = row
        new_col = col

    agent = (new_row, new_col)


    reward = leaving_reward
    done = False

    if agent == GOAL:
        reward = 1
        done = True

    elif agent == TRAP:
        reward = -1
        done = True
    
    
    return agent, reward, done



def render(agent):

    print()

    for r in range(ROWS):

        for c in range(COLS):

            if (r, c) == agent:
                text = " A "

            elif (r, c) == START:
                text = " S "

            elif (r, c) == GOAL:
                text = "+1 "

            elif (r, c) == TRAP:
                text = "-1 "

            elif (r, c) == WALL:
                text = "XXX"

            else:
                text = "   "

            print(f"|{text}", end="")

        print("|")

        print("+---"*COLS + "+")



def print_policy():

    arrows = [chr(0x2191), chr(0x2192), chr(0x2193), chr(0x2190)] # up , right , down , left arrow unicode
    

    print()

    for r in range(ROWS):

        for c in range(COLS):

            position = (r, c)

            if position == WALL:
                print(" X ", end="")

            elif position == GOAL:
                print(" + ", end="")

            elif position == TRAP:
                print(" - ", end="")

            else:

                state = state_dict[position]

                best_action = np.argmax(Q[state])

                print(f" {arrows[best_action]} ", end="")

        print()

    print()





def choose_action(state, epsilon):

    if random.random() < epsilon:
        return random.randint(0, 3)

    return np.argmax(Q[state])



def generate_episode(epsilon):

    episode = []

    agent = reset()

    done = False

    while not done:

        state = get_state(agent)

        action = choose_action(state, epsilon)

        next_agent, reward, done = step(agent, action , LEAVING_REWARD)

        episode.append((state, action, reward))

        agent = next_agent

    return episode



def monte_carlo_update(episode):

    G = 0

    visited = []

    for state, action, reward in reversed(episode):

        G = reward + gamma * G

        if (state, action) in visited:
            continue

        visited.append((state, action))

        if (state, action) not in returns:
            returns[(state, action)] = []

        returns[(state, action)].append(G)

        Q[state][action] = np.mean(returns[(state, action)])




Q = np.zeros((11, 4))


# monte_carlo
returns = {}
gamma = 0.9
epsilon = 0.2

for i in range(5000):

    episode = generate_episode(epsilon)

    monte_carlo_update(episode)

    if i % 1000 == 0:

        print("=" * 40)

        print("Episode:", i)

        print("Steps:", len(episode))

        print_policy()

        print("=" * 40)

print(episode)



# Q-learning

# alpha = 0.1
# gamma = 0.9
# epsilon = 0.2

# for episode in range(5000):

#     agent = reset()

#     done = False

#     while not done:

#         state = get_state(agent)

#         action = choose_action(state, epsilon)

#         next_agent, reward, done = step(agent, action , LEAVING_REWARD)

#         next_state = get_state(next_agent)

#         # Q-Learning Update
#         target = reward + gamma * np.max(Q[next_state])

#         error = target - Q[state][action]

#         Q[state][action] += alpha * error

#         agent = next_agent

#     if episode % 100 == 0:

#         print(f"\nEpisode {episode}")

#         print_policy()



# SARSA

# alpha = 0.1
# gamma = 0.9
# epsilon = 0.2
# for episode in range(5000):

#     agent = reset()

#     state = get_state(agent)

#     action = choose_action(state, epsilon)

#     done = False

#     while not done:

#         next_agent, reward, done = step(agent, action , LEAVING_REWARD)

#         next_state = get_state(next_agent)

#         if done:

#             target = reward

#         else:

#             next_action = choose_action(next_state, epsilon)

#             target = reward + gamma * Q[next_state][next_action]

#         Q[state][action] += alpha * (target - Q[state][action])

#         agent = next_agent
#         state = next_state

#         if not done:
#             action = next_action

#     if episode % 100 == 0:

#         print(f"\nEpisode {episode}")

#         print_policy()
def print_policy():

    arrows = [chr(0x2191), chr(0x2192), chr(0x2193), chr(0x2190)] # up , right , down , left arrow unicode
    

    print()

    for r in range(ROWS):

        for c in range(COLS):

            position = (r, c)

            if position == WALL:
                print(" X ", end="")

            elif position == GOAL:
                print(" + ", end="")

            elif position == TRAP:
                print(" - ", end="")

            else:

                state = state_dict[position]

                best_action = np.argmax(Q[state])

                print(f" {arrows[best_action]} ", end="")

        print()

    print()





def choose_action(state, epsilon):

    if random.random() < epsilon:
        return random.randint(0, 3)

    return np.argmax(Q[state])



def generate_episode(epsilon):

    episode = []

    agent = reset()

    done = False

    while not done:

        state = get_state(agent)

        action = choose_action(state, epsilon)

        next_agent, reward, done = step(agent, action , LEAVING_REWARD)

        episode.append((state, action, reward))

        agent = next_agent

    return episode



def monte_carlo_update(episode):

    G = 0

    visited = []

    for state, action, reward in reversed(episode):

        G = reward + gamma * G

        if (state, action) in visited:
            continue

        visited.append((state, action))

        if (state, action) not in returns:
            returns[(state, action)] = []

        returns[(state, action)].append(G)

        Q[state][action] = np.mean(returns[(state, action)])




Q = np.zeros((11, 4))


# monte_carlo
# returns = {}
# gamma = 0.9
# epsilon = 0.2

# for i in range(5000):

#     episode = generate_episode(epsilon)

#     monte_carlo_update(episode)

#     if i % 1000 == 0:

#         print("=" * 40)

#         print("Episode:", i)

#         print("Steps:", len(episode))

#         print_policy()

#         print("=" * 40)

# print(episode)



# Q-learning

alpha = 0.1
gamma = 0.9
epsilon = 0.2

for episode in range(5000):

    agent = reset()

    done = False

    while not done:

        state = get_state(agent)

        action = choose_action(state, epsilon)

        next_agent, reward, done = step(agent, action , LEAVING_REWARD)

        next_state = get_state(next_agent)

        # Q-Learning Update
        target = reward + gamma * np.max(Q[next_state])

        error = target - Q[state][action]

        Q[state][action] += alpha * error

        agent = next_agent

    if episode % 100 == 0:

        print(f"\nEpisode {episode}")

        print_policy()



# SARSA

# alpha = 0.1
# gamma = 0.9
# epsilon = 0.2
# for episode in range(5000):

#     agent = reset()

#     state = get_state(agent)

#     action = choose_action(state, epsilon)

#     done = False

#     while not done:

#         next_agent, reward, done = step(agent, action , LEAVING_REWARD)

#         next_state = get_state(next_agent)

#         if done:

#             target = reward

#         else:

#             next_action = choose_action(next_state, epsilon)

#             target = reward + gamma * Q[next_state][next_action]

#         Q[state][action] += alpha * (target - Q[state][action])

#         agent = next_agent
#         state = next_state

#         if not done:
#             action = next_action

#     if episode % 100 == 0:

#         print(f"\nEpisode {episode}")

#         print_policy()
