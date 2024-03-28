# Given a method biased_toss() that generates 0 or 1. 
# It generates 1 with some probability p (not necessarily 0.5). 
# Write a method that generates 0 or 1 with probability 0.5.

def solution():
    while True:
        a = biased_toss()
        b = biased_toss()
        if a ^ b:
            return a
