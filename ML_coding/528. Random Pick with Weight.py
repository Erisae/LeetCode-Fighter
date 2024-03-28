class Solution:

    def __init__(self, w: List[int]):
        curSum = 0
        self.grid = []
        for w1 in w:
            curSum += w1
            self.grid.append(curSum)
            

    def pickIndex(self) -> int:
        num = random.random() * self.grid[-1]
        # find in which interval
        for idx, v in enumerate(self.grid):
            if num < v:
                return idx
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()