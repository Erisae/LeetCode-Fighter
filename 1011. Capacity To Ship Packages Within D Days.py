class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        minCapacity = math.ceil(sum(weights) / days)
        # search from minCapacity and greedy
        cap = minCapacity
        n = len(weights)
        while True:
            numDay = [cap] * days
            idx = 0
            for i in range(days):
                while idx < n:
                    if numDay[i] < weights[idx]:
                        break
                    else:
                        numDay[i] -= weights[idx]
                        idx += 1
            if idx >= n:
                break
            else:
                cap +=1 
        
        return cap
                
