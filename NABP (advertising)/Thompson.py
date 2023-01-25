import pandas as pd  #to read the dataset
import random #to select random x (theta) values from the distribution graphs of bandits


dataset = pd.read_csv('C:\\Users\\Samruddhi\\Desktop\\Reinforcement learning\\NABP (advertising)\\Dataset\\Ads_CTR_Optimisation.csv')
# rows = epochs = user
# columns = n = ad number


############# thompson sampling implementation ################################
epochs = 10000 #also the total number of users
n = 10 #number of bandits (ads)
    #ad index: 0 to n-1


#attributes of each ad
k = [0] * n
    #k[i] = number of times the ith ad was selected
p = [0] * n
    #p[i] = number of times ad i resulted in success
q = [0] * n
    #q[i] = number of times ad i resulted in failure
#for each ad: p+q=k

theta = [0]*n  
    #theta[i] = theta value for the ith ad for the given episode

#training
for ep in range(0, epochs):
    #find theta for each ad
    for i in range(0,n) :
        theta[i] = random.betavariate(p[i] + 1, q[i] + 1)

    #select the ad with the max theta value
    ad = theta.index(max(theta)) 

    #the reward for pulling this ad
    reward = dataset.values[ep, ad]

    #update attributes for this ad
    k[ad] = k[ad] + 1
    if reward==0 :
        #failure
        q[ad] = q[ad] + 1
    else:
        #success
        p[ad] = p[ad] + 1



######  training completed  #######################################################
#success rate of ad = p/k
#print results
print("Results: ")
for i in range(0,n) :
    print(f"Bandit {i} was pulled {k[i]} number of times. Its success rate is { p[i]/k[i]}\n")



