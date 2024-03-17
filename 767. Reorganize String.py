class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s) # count of each character
        pq = [] # (-count, char)
        for c, count in counter.items():
            heapq.heappush(pq, (-count, c))
        
        # every time, pop left most.  
        result = ""
        n = len(s)
        freeze = None # -count, c

        for i in range(n):
            if not pq:
                return ""
            count, c = heapq.heappop(pq)
            result += c
            if freeze:
                heapq.heappush(pq, freeze)
            if count + 1 == 0: # used up
                freeze = None
            else:
                freeze = (count + 1, c)
        return result
        