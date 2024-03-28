import numpy as np 

def logistic_loss(y_true, y_pred):
    # clip y_pred to avoid log of 0 and 1
    y_pred = np.clip(y_pred, 1e-9, 1 - 1e-9)
    loss = - np.mean(y_true * np.log(y_pred) + (1-y_true) * np.lod(1-y_pred))

    return loss
