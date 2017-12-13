import gym
env = gym.make('AirRaid-ram-v0')
for i_episode in range(1):
    observation = env.reset()  # reset for each new trial
    for t in range(1000):  # run for 100 timesteps or until done, whichever is first
        env.render()
        # select a random action (see https://github.com/openai/gym/wiki/CartPole-v0)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        print("Reward", reward, done, info)
        if done:
            print("Episode finished after {} timesteps".format(t + 1))
            print(observation, )
            print("Reward", reward, done, info)
            break
