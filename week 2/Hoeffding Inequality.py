import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt 
from tqdm import tqdm

class coin:
    def __init__(self,n_coins, n_flips):
        self.n_coins = n_coins
        self.n_flips = n_flips
        self.flip_history = np.zeros(self.n_coins * self.n_flips).reshape([self.n_coins, self.n_flips])
        self.proportions_head = np.zeros(self.n_coins)
    
    def flip_coins(self):
        for coin in range(self.n_coins):
            self.flip_history[coin,:] = np.random.randint(0,2,self.n_flips)

    def get_proportions_head(self):
        for coin in range(self.n_coins):
            self.proportions_head[coin] = np.sum(self.flip_history[coin,:]) / self.n_flips

    
def train(iterations):
    v1 = []
    v2 = []
    v3 = []

    for i in tqdm(range(iterations)):
        i = 1
        flip = coin(1000*i,10)
        flip.flip_coins()
        flip.get_proportions_head()
        c1 = 0
        crand = np.random.randint(0,1000,1)
        cmin = np.argmin(flip.proportions_head)

        v1.append(flip.proportions_head[c1])
        v2.append(flip.proportions_head[crand])
        v3.append(flip.proportions_head[cmin])
        
    return v1,v2,v3


v1,v2, v3 = train(10000)

"""
for v, name  in zip([v1,v2,v3],["v1","v2","v3"]):
    print("{}".format(name), "has a mean of" ,np.mean(v))

sns.distplot(v1)
sns.distplot(v2)
sns.distplot(v3)
plt.show()
"""

"""
means after 100000 runs:

v1: .50168
v2: .50152
v3: .03763

"""









