import numpy as np

def softmax(x):
    # exp(x) -> has a high probability of overflow, then deduct max
    exp_x = np.exp(x - np.max(x))
    return exp_x / exp_x.sum(axis=1, keep_dim=True)

    # axis -> add along axis
    # x_j-> x at jth class