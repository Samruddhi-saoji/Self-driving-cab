import gym
import numpy as np
from numpy.random import random
from random import randint
import matplotlib.pyplot as plt

env = gym.make("Taxi-v3").env


class Taxi :
    def __init__(self) -> None:  
        #the Q table
        self.q_table = np.zeros([env.observation_space.n, env.action_space.n]) #500x6 matrix

        #lists maintaining the total timesteps recquired in each learning episode
        self.timesteps = []

    #training the agent
    def train(self) :
        for i in range(episodes) :
            state = env.reset() #resets the env to a random starting state

            epochs = 0 #count of timesteps
            done = False #is the passenger dropped at the correct destination?
            tot_reward = 0 #tot reward collected at the end of an episode

            while not done:
                #choose action
                action = self.select_action(state)

                #perform the action
                next_state, reward , done , info = env.step(action)
                #env.step(action) performs the action and returns the result of the action
                #result = next state, reward of this action, is the passenger dropped correctly? , misc info

                #update the Q table
                self.update(state, action, next_state, reward)

                #update the current state
                state = next_state

                #increment timestep
                epochs += 1

            #this episode is complete
            #update the stats lists
            self.timesteps.append(epochs)

        #learning is complete
        print("Training completed.")
    
        #show the stats
        self.display_stats()


    #selecting the action
    def select_action(self, state) :
        #explore epsilon % of the times
        if random() < epsilon :
            #explore 
            action = env.action_space.sample() #retruns random action from action space
        else:
            #exploit the current best action
            action = np.argmax(self.q_table[state])
            #argmax(arr[row]) returns the max value in that row
        return action


    #updating the Q table
    def update(self, state, action, next_state, reward) :
        old_q = self.q_table[state, action]

        #the maximum q value in the next state
        q_max = np.max(self.q_table[next_state])
        
        #calculate the new q value
        new_q = (1 - alpha) * old_q + alpha * (reward + gamma * q_max)

        #enter the new q value
        self.q_table[state, action] = new_q


    #plot the graphs
    def display_stats(self) :
        #x axis = episode number
        x_points = np.array(range(1,episodes + 1))

        #time steps graph#######################
        plt.plot(x_points, self.timesteps)

        #labelling
        plt.title('Timesteps per episode')
        plt.xlabel('Episode')
        plt.ylabel('Timesteps')

        #print graph
        plt.show()



################################################
#driver code
if __name__ == "__main__" :
    #hyperparameters
    alpha = 0.1
    gamma = 0.6
    epsilon = 0.1

    episodes = 100

    taxi = Taxi()
    taxi.train()

    


