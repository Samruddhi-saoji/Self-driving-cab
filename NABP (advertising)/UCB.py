import pandas as pd  #to read the dataset
import math #square root to calculate diff


dataset = pd.read_csv('C:\\Users\\Samruddhi\\Desktop\\Reinforcement learning\\NABP (advertising)\\Dataset\\Ads_CTR_Optimisation.csv')
# rows = epochs, columns = n


############# UCB implementation #####################
epochs = 10000 #also the total number of users
n = 10 #number of bandits (ads)
    #ad index: 0 to n-1


#attributes of each ad
k = [0] * n
    #k[i] = k value for the ith ad
Q_k = [0] * n
    #Q_k[i] = Q value for ith ad, where ad has been selected k times before

UCB = [1]*n  #UCB[i] = UCB value for the ith ad
    #initially, upper limit is 1 for all

#training
for ep in range(1, epochs+1):
    ad = UCB.index(max(UCB)) #return index of the max element in list UCB

    #check the reward for this ad
    #r_k+1
    reward = dataset.values[ep-1, ad]
        # dataset[row][col]  #row index starts from 0 and ep starts from 1

    #update parameters
    #Q_k+1 = (k*Q_k + r_k+1)/(k+1)
    Q_k[ad] = (k[ad]*Q_k[ad] + reward)/(k[ad] + 1)
    k[ad] += 1

    #diff
    diff = math.sqrt(3/2 * math.log(ep) / k[ad] )

    #UCB = Q + diff
    UCB[ad] = Q_k[ad] + diff


#training completed
#print results
print("Results: ")
for i in range(0,n) :
    print(f"Bandit {i} was pulled {k[i]} number of times. Its expected reward is {Q_k[i]}\n")




