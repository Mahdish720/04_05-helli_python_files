import gymnasium as gym
import numpy as np
import random

env = gym.make('FrozenLake-v1', desc = None , map_name = '4x4' , is_slippery = False , render_mode = 'human' , reward_schedule = (1,-1,-0.05))
# env = gym.make('FrozenLake-v1', desc = None , map_name = '4x4' , is_slippery = False , reward_schedule = (1,-1,-0.05))

num_states = env.observation_space.n
num_actions = env.action_space.n

alpha = 0.1
gamma = 0.9
epsilon = 0.2




def choose_action(state, epsilon):
    if random.random() < epsilon:
        return env.action_space.sample() 
    return np.argmax(Q[state])


def generate_episode(epsilon):
    episode = []
    
    state, info = env.reset()
    
    done = False
    
    while not done:
        action = choose_action(state, epsilon)
        

        next_state, reward, terminated, truncated, info = env.step(action)
        
        done = terminated or truncated
        
        episode.append((state, action, reward))
        state = next_state
        
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
        
        # آپدیت مقدار Q با میانگین پاداش‌ها
        Q[state][action] = np.mean(returns[(state, action)])
        
# Q = np.zeros((num_states, num_actions))
# returns = {} # monte carlo
# print("Training with Monte Carlo...")
# for i in range(5000):
#     ep = generate_episode(epsilon)
#     monte_carlo_update(ep)
    
    
    
# Q = np.zeros((num_states, num_actions))
# print("Training with Q-Learning...")
# for episode in range(5000):
#     state, info = env.reset()
#     done = False
    
#     while not done:
#         action = choose_action(state, epsilon)
        
#         next_state, reward, terminated, truncated, info = env.step(action)
#         done = terminated or truncated
        
#         target = reward + gamma * np.max(Q[next_state])
#         error = target - Q[state][action]
#         Q[state][action] =  Q[state][action] + alpha * error
        
#         state = next_state
        
        
Q = np.zeros((num_states, num_actions))
print("Training with SARSA...")
for episode in range(5000):
    state, info = env.reset()
    action = choose_action(state, epsilon)
    done = False
    
    while not done:
        next_state, reward, terminated, truncated, info = env.step(action)
        done = terminated or truncated
        
        if done:
            target = reward
        else:
            next_action = choose_action(next_state, epsilon)
            target = reward + gamma * Q[next_state][next_action]
            
        Q[state][action] = Q[state][action] + alpha * (target - Q[state][action])
        
        state = next_state
        if not done:
            action = next_action