class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        pq = []
        heapq.heappush(pq, (-a, 0))
        heapq.heappush(pq, (-b, 1))
        heapq.heappush(pq, (-c, 2))

        m = "abc"
        res = ""

        last = -1

        maxVal = 0
        maxIdx = 0
        usage = 0

        while True:
            val, idx = heapq.heappop(pq)
            if idx == last: # same, should pop another
                maxVal, maxIdx = heapq.heappop(pq)
                heapq.heappush(pq, (val, idx)) # push back unused
                val, idx = maxVal, maxIdx

            # calculate usage
            if val == 0:
                break
            if val < pq[0][0]: # the actual maximum, use up to 2
                usage = min(2, -val)
            else:
                usage = 1
            
            res += m[idx] * usage
            heapq.heappush(pq, (val + usage, idx))
            last = idx

        return res

            
                