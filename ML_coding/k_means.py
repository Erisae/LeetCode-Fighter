import numpy as np

def initialize_centroids(data, k):
    # randomly pick k points from data
    indices = np.random.choice(data.shape[0], size=k, replace=False)
    return data[indices]

def closest_centroids(data, centroids):
    # compute data point to each of its closest centroids
    minIndices = []
    for point in data:
        minDist = np.inf
        minIdx = -1
        for idx, centroid in enumerate(centroids):
            dist = np.sqrt(np.sum((data - centroid)**2))
            if dist < minDist:
                minDist = dist
                minIdx = idx
        minIndices.append(minIdx)
    return minIndices

def move_centroids(data, centroids, closest):
    # ith new_centroid -> the average of all data that is closest to ith centroid
    return np.array([data[closest==k].mean(axis=0) for k in range(centroids.shape[0])])


def k_means(data, k, max_iterations):
    centroids = initialize_centroids(data, k)
    for i in range(max_iterations):
        closest = closest_centroids(data, centroids)
        new_centroids = move_centroids(data, centroids, closest)
        if np.all(new_centroids == centroids):
            break
        centroids = new_centroids
    return centroids
