import numpy as np

def t_test_one_sample(x, mu0):
    """
    Compute one-sample t-statistic.
    """
    # Write code here
    x = np.array(x,dtype=float)
    n = x.size
    x_bar = np.mean(x)
    s = np.std(x,ddof=1)
    t_stat = (x_bar-mu0)/(s/(np.sqrt(n)))
    return float(t_stat)
    pass