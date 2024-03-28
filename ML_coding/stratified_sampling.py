'''
Implement Stratified sampling.

Given training data, class labels and the fraction of validation data per class 'test_size'. 
Write a method to sample train data, test data, train labels and test labels 
such that each class has 'test_size' fraction of data/labels for validation and 1-test_size fraction of data/labels for training.
'''
import numpy as np 
import random

data = np.zeros((10000, 10))
label = np.array((10000, 2))
test_size = 0.7

index_range = list(range(data.shape[0]))
num = int(data.shape[0] * test_size)

test_index = random.sample(index_range, num)
train_index = [item for item in index_range if item not in test_index]

val_data = data[test_index]
val_label = label[test_index]
train_data = data[train_index]
train_label = label[train_index]

