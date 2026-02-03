import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    # Write code here
    arr = np.array(x,dtype=float)
    mean = np.mean(arr)
    siz = arr.size
    var= np.sum((arr-mean)**2)/(siz-1)
    sd = np.sqrt(var)
    return (float(var),float(sd))
    pass