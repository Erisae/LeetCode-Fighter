class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n - 1
        maxSize = 0
        while left < right:
            maxSize = max(maxSize, (right - left) * min(height[left], height[right]))
            # when move left and right -> since idx diff decrease, should go to the shorter direction
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxSize