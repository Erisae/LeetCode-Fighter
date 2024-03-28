class Solution:

    def __init__(self, nums: List[int]):
        self.array = nums
        self.last = self.array

    def reset(self) -> List[int]:
        return self.array

    def shuffle(self) -> List[int]:
        # randomly shuffle
        copy = self.last.copy()
        n = len(copy)
        for i in range(n):
            j = random.randint(i, n - 1)
            copy[i], copy[j] = copy[j], copy[i]
        self.last = copy
        return copy


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()