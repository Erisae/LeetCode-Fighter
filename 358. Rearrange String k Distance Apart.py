class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k <= 1:
            return s
        # feels like the k inetrval, max heapq
        counter = Counter(s) 
        maxHeap = []
        for key, value in counter.items():
            heapq.heappush(maxHeap, (-value, key)) # count and char
        
        frozen = {}
        result = ""
        # k is freeze time
        while maxHeap:
            count, ch = heapq.heappop(maxHeap)
            result += ch
            
            # frozen 
            delete = []
            for key, value in frozen.items():
                frozen[key][0] -= 1
                if frozen[key][0] == 0:
                    heapq.heappush(maxHeap, (frozen[key][1], key))
                    delete.append(key)
            for key in delete:
                del frozen[key]

            # put into frozen
            if count + 1 < 0:
                frozen[ch] = [k - 1, count + 1]
        
        if frozen:
            return ""
        return result
            