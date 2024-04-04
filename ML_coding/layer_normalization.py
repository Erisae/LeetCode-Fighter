import numpy as np

def layer_normalization(X, epsilon=1e-5):
    X_mu = np.mean(X, axis=1, keep_dim=True)
    X_var = np.var(X, axis=1, keep_dim=True)

    X_normalized = (X - X_mu) / np.sqrt(X_var + epsilon)
    gamma = np.ones((1, X.shape[1]))
    beta = np.zeros((1, X.shape[1]))

    # originally it is 0 mean and 1 variance
    out = gamma * X_normalized + beta

    cache = (X, X_mu, X_var, X_normalized, gamma, beta, epsilon)
    return out, cache