from numpy.random import random
from random import randint


#################################
#bandit class
class Bandit:
    #constructor
    def __init__(self,id, srate) -> None:
        self.Q = 0 #Qk(a) = expected reward for pulling bandit 

        self.k = 0 #number of times this bandit has been pulled

        self.id = id #id of the bandit

        self.srate= srate #success rate of the bandit

    #when the bandit is pulled, the result is either win or loss
    # for win, reward = 1  #for loss rewrd = 0
    # probability of win = success rate of the bandit
    def pull(self) :
        #generate a random num btw 0 and 1
        #if the number is less than success rate, then its a win
        if random() < self.srate :
            return 1
        else:
            return 0


############################################

class NArmedBandit :
    def __init__(self, prob_list, id_list) -> None:
        #prob_list[i] = success rate of the ith bandit
        #id_list[i] = id of the ith bandit

        self.bandits = [] #list of the n bandits

        #create each bandit and add it to the list
        for i in range (0,n) :
            id = id_list[i]
            srate = prob_list[i]
            self.bandits.append(Bandit(id, srate))


    #play the game
    def run(self) :
        print(self.bandits)
        for i in range(episodes) :
            #select the bandit to pull
            indx = self.select_bandit()
            bandit = self.bandits[indx]

            #pull the bandit
            reward = bandit.pull()

            #update the results of this iteration
            self.update(bandit, reward)

            #show the entire training process
            print(f"\nIteration {i} , bandit {bandit.id} pulled. Q value = {bandit.Q}")
        print() 


    #select bandit function
    #returns index of the selected bandit
    def select_bandit(self) :
        #epsilon greedy strategy
        #explore epsilon % of the times
        if random() < epsilon :
            #explore #chose any bandit at random
            indx = randint(0, n-1) #[0,n-1]
        else:
            #exploit the current best bandit
            indx = self.get_best_bandit()
        return indx


    #return the index of bandit with the max Q_k+1 value
    def get_best_bandit(self):
        indx = 0
        max = self.bandits[0].Q #the max yet Q val

        #check each bandit and find the max
        for i in range(0, n) :
            #if this bandits Q val is higher than max
            if self.bandits[i].Q > max :
                max = self.bandits[i].Q
                indx = i

        return indx


    #update the value of k and Q value for the bandit
    def update(self, bandit, reward) :
        #the recursive formula for Q value
        #Q_k+1 = (k*Q_k + r_k+1)/k+1
        bandit.Q = (bandit.k*bandit.Q  +  reward)/(bandit.k + 1)

        bandit.k = bandit.k + 1  #k--->k+1


    #show stats
    def show_stats(self) :
        #show how many times each bandit was pulled
        for i in range(0,n) :
            print(f"\nBandit {self.bandits[i].id} was pulled {self.bandits[i].k} times.")


################################################
#driver code

if __name__ == "__main__" :
    #the game parameters#############
    epsilon = 0.3  #probability of exploration
    n = 5 #number of bandits
    prob_list = [0.2 ,0.5, 0.7 , 0.4 , 0.1] #success rates of bandits
    id_list = [1,2,3, 4, 5] #id of the bandits
    episodes = 1000 #number of iterations in which the gaent can learn

    #create the game
    NABP = NArmedBandit(prob_list, id_list)
    #play
    NABP.run()

    #now lets see the results
    NABP.show_stats()
    #the bandit with the max success rate should be pulled the highest number of times

