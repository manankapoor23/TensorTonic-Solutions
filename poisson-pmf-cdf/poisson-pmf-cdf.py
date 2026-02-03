import numpy as np
import math 
def poisson_pmf_cdf(lam, k):
    """
    Compute Poisson PMF and CDF.
    """
    # Write code here
    # here lamda is the average rate of that event
    # k is the number of events
    pmf = (np.exp(-lam)*np.power(lam,k))/math.factorial(k)
    cdf = 0.0
    for i in range(k+1):
        cdf+= ((np.exp(-lam)*np.power(lam,i))/math.factorial(i))
    return (float(pmf),float(cdf))
    


    pass