import numpy as np 
from tqdm import tqdm

class data:

    def __init__ (self, N):
        self.d = 2
        self.N = N
        self.a = 0
        self.b = 0
        self.X = np.zeros((self.N, self.d))
        self.y = np.zeros(self.N)
        
    def generate_function(self):
        x = np.random.uniform(-1,1,2)
        y = np.random.uniform(-1,1,2)

        self.a, self.b = np.polyfit(x,y,1)

    def generate_points(self):
        self.X = np.random.uniform(-1,1,(self.N, self.d))
        i = 0
        for x in self.X:
            if x[1] > ((self.a * x[0] + self.b)):
                self.y[i] = 1
            else:
                self.y[i] = -1
            
            i += 1


def train(N,i):
    hypotheses = {}

    running_total_in = 0
    running_total_out = 0

    # In sample
    for i in tqdm(range(i)):
        session = data(N)
        session.generate_function()
        session.generate_points()

        X,y = session.X,session.y

        psudo_inverse = np.linalg.inv(X.T@X)@X.T
        w = psudo_inverse@y

        # Measure error
        y_prime = np.sign(X@w)
        error = y-y_prime
        error = np.abs(np.sum(error))/2
        error_rate = error/len(y)

        running_total_in += error_rate
        hypotheses["{}".format(w)] = error_rate

        
        # Out of sample
    
        session_new = data(N)
        session_new.generate_function()
        session_new.generate_points()

        X_new,y_new = session_new.X, session_new.y

        # Measure error
        y_prime = np.sign(X_new@w)
        error = y_new - y_prime
        error = np.abs(np.sum(error))/2
        error_rate = error/len(y)

        running_total_out += error_rate
    
    return running_total_in/i, running_total_out/i

print(train(100,10000))