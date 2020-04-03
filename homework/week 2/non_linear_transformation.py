import numpy as np 
from tqdm import tqdm

class data:

    def __init__(self, N):
        self.N = N
        self.d = 2
        self.X = np.zeros((self.N, self.d))
        self.y = np.zeros(self.N)

    def generate_points(self):
        self.X = np.random.uniform(-1,1,(self.N, self.d))
        self.y = np.sign(self.X.sum(axis = 1) - 0.6)
        self.X = np.c_[np.ones(self.N),self.X]
        # Add noise
        idx = np.random.randint(0, self.N, int(np.round(self.N * .1, 0)))
        self.y[idx] = self.y[idx] * -1
        
def train(N,i, transformation = False):

    hypotheses = {}

    running_total_in = 0

    # In sample
    for i in tqdm(range(i)):
        session = data(N)
        session.generate_points()

        X,y = session.X,session.y

        if transformation == True:
            X = np.c_[X, np.multiply(X[:,1], X[:,2]), np.multiply(X[:,1], X[:,1]), np.multiply(X[:,2], X[:,2])]


        psudo_inverse = np.linalg.inv(X.T@X)@X.T
        w = psudo_inverse@y

        # Measure error
        y_prime = np.sign(X@w)
        error = y-y_prime
        error = np.abs(np.sum(error))/2
        error_rate = error/len(y)

        running_total_in += error_rate
        hypotheses["{}".format(w)] = error_rate

    return hypotheses#running_total_in / i

print(train(1000,10, transformation=True))



