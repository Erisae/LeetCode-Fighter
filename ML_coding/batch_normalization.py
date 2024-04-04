import numpy as np

def bacth_normalization(X_train, gamma, beta, epsilon=1e-5):
    '''
    X: Input data of shape (N,D) D is feature size
    gamma: Scale parameter, shape(D,)
    beta: Shift parameterm shape(D,)
    epsilon: Small float added to variance to avoid deviding by zero

    Returns:
    - out: batch-normalized data
    - cache: tuple of values needed in the backward pass
    '''
    X_mu = np.mean(X_train, axis=0)
    X_var = np.var(X_train, axis=0)

    X_normalized = (X_train - X_mu) / np.sqrt(X_var + epsilon)
    X_out = gamma * X_normalized + beta

    # cache for backward pass
    cache = (X_train, X_normalized, X_mu, X_var, gamma, beta, epsilon)

    return X_out, cache