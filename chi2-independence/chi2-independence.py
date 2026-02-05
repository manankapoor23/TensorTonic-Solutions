import numpy as np

def chi2_independence(C):

    C = np.asarray(C, dtype=float)

    # Row sums, column sums, total
    row_sums = C.sum(axis=1)
    col_sums = C.sum(axis=0)
    total = C.sum()

    # Expected frequencies using outer product
    expected = np.outer(row_sums, col_sums) / total

    # Chi-square statistic
    chi2 = np.sum((C - expected) ** 2 / expected)

    return chi2, expected