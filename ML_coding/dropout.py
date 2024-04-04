import numpy as np

def dropout(X_train, dropout_rate):
    if not dropout_rate:
        return X_train, np.ones_like(X_train)
    mask = np.random.rand(*X_train.shape) > dropout_rate
    X_dropout = mask * X_train

    # important
    X_dropout = X_dropout / (1.0 - dropout_rate) # maintain the expected sum **
    return X_dropout, mask
    