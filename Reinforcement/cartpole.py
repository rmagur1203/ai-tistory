import gymnasium as gym
import tensorflow as tf
import numpy as np
import random
import os
from collections import deque

env = gym.make('CartPole-v1', render_mode='human')

model = tf.keras.Sequential([
    tf.keras.layers.Dense(32, activation='relu', input_shape=(4,)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(2, activation='linear'),
])

model.compile(optimizer='adam', loss='mse', metrics=['accuracy'])

checkpoint_path = "Reinforcement/model.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)

model.load_weights(checkpoint_path)

observation, info = env.reset()
state = np.array([observation]).reshape([1, 4])

for t in range(500):
    env.render()
    
    predict = model.predict(state, verbose=0)
    action = np.argmax(predict)
    
    prev_state = state
    observation, reward, terminated, truncated, info = env.step(action)
    state = np.array([observation]).reshape([1, 4])

    if terminated or truncated:
        print('Episode finished after {} timesteps'.format(t + 1))
        print('terminated', terminated)
        print('truncated', truncated)
        break
env.close()
