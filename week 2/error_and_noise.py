"""
3)

Hypothesis has an error rate of mu when approximating a deterministic function. Same hypothesis correctly classifies y=f(x) with probability lambda. 

Therefore, the probability of error h makes is:

    y != f(x) = 1-lambda
    this is made with error 1-mu
    therefore the first part of our equation is: 1-mu*(1-lambda)

    y = f(x) = lambda
    this is made with error mu
    therefore the second part of out equation is: mu * lambda

    therefore out final probabiluity is:

    1-mu(1-lambda) + (mu*lambda) == [e]

"""

"""
4)

when lambda = 0.5, we have:

    (1-mu * 0.5) + (mu * 0.5)

    note that mu + 1-mu = 1

    therefore, for any value of mu, this equation will equal 1.

    Therefore, wheen lambda = 0.5, the probability is independant of mu. == [b]


"""