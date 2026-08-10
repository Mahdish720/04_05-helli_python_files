import gymnasium as gym
import numpy as np
import random

env = gym.make('CartPole-v1')


Q = np.zeros((10, 10, 10, 10, 2))



def value_to_box(value, min_val, max_val, num_boxes=10):

    if value <= min_val:
        return 0
        
    if value >= max_val:
        return num_boxes - 1
        
    percent = (value - min_val) / (max_val - min_val)
    

    box_number = int(percent * num_boxes)
    
    return box_number


def get_discrete_state(state):

    pos_box = value_to_box(state[0], min_val=-2.4, max_val=2.4)
    
    vel_box = value_to_box(state[1], min_val=-3.0, max_val=3.0)
    
    ang_box = value_to_box(state[2], min_val=-0.25, max_val=0.25)
    
    ang_v_box = value_to_box(state[3], min_val=-2.0, max_val=2.0)
    
    return (pos_box, vel_box, ang_box, ang_v_box)


alpha = 0.1
gamma = 0.99 
epsilon = 0.2

print("Training is starting... Please wait.")

for episode in range(5000):
    
    state_raw, info = env.reset()
    state = get_discrete_state(state_raw)
    
    done = False
    
    while not done:
        if random.random() < epsilon:
            action = env.action_space.sample()
        else:
            action = np.argmax(Q[state])
            
        next_state_raw, reward, terminated, truncated, info = env.step(action)
        done = terminated or truncated
        
        next_state = get_discrete_state(next_state_raw)
        
        target = reward + gamma * np.max(Q[next_state])
        error = target - Q[state][action]
        Q[state][action] += alpha * error
        
        state = next_state

print("Training finished! Let's watch it play.")


env_visual = gym.make('CartPole-v1', render_mode="human")
state_raw, info = env_visual.reset()
state = get_discrete_state(state_raw)
done = False

while not done:
    action = np.argmax(Q[state])
    state_raw, reward, terminated, truncated, info = env_visual.step(action)
    state = get_discrete_state(state_raw)
    done = terminated or truncated

env_visual.close()