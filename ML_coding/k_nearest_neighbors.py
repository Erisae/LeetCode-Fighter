import numpy as np

def k_nearest_neighbors(data, query, k, distance_fn, choice_fn):
    # calculate distance between each query and data

    distance_save = []
    for idx, (feature, _) in enumerate(data):
        distance_save.append([distance_fn(feature, query), idx]) # distance, index
    
    # sort
    distance_save.sort(key = lambda x: x[0]) # sort according to distance
    # find minimal k
    labels = [data[idx][1] for _,idx in distance_save[:k]]
    target = choice_fn(labels)

    return target

"""
data and query, get k nearest neighbor of query in data and get label according to that
"""

def euclidean_distance(data1, data2):
    distance = np.sqrt(np.sum((data1 - data2)**2))
    return distance

def max_voting(labels):
    counter = Counter(labels)
    return counter.most_common(1)[0]