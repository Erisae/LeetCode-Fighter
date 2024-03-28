def auc_roc(predictions, true_labels):
    y = zip(predictions, true_labels)
    y.sort(key = lambda x : x[0])

    # calculate positive and negative
    positive = sum([j for _,j in y])
    negative = sum([(1 - j) for _,j in y])

    #
    prev_tpr, prev_fpr = 0, 0
    tp, fp = 0, 0
    n = len(predictions)
    area = 0

    for i in range(n - 1, -1, -1):
        # suppose the threshold now is y[i][0]
        if y[i][0] == 1:
            tp += 1
        else:
            fp += 1
        tpr = tp / positive if positive > 0 else 0
        fpr = fp / negative if negative > 0 else 0
        area += (fpr - prev_fpr) * (tpr + prev_tpr) / 2

        prev_tpr = tpr
        prev_fpr = fpr
    
    return area
