import numpy as np
from collections import Counter

def mean_median_mode(x):
    arr = np.array(x)
    mean = np.mean(arr)
    median = np.median(arr)
    values , counts = np.unique(x,return_counts=True)
    mode = values[counts==counts.max()].min()
    mean = float(mean)
    median = float(median)
    modes = float(mode)
    return (mean,median,modes)
    pass