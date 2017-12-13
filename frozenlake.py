
import gym
import numpy as np


env = gym.make('FrozenLake-v0')


for i_episode in range(2):
    observation = env.reset()
    for i in range(100):
        env.render()
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        print("Action {} and observation {} in episode {}, step {}".format(
            action, observation, i_episode, i))
        if done:
            print("Episode finished after {} timesteps".format(i + 1))
            break
