import gym
import time
env = gym.make('CartPole-v0')

state = env.reset()

for t in range(10000):
    env.render()
    print(state)

    action = env.action_space.sample()
    state,reward,done,info = env.step(action)
    time.sleep(1)
    if done:
        print("Finished")
        break


env.close()
