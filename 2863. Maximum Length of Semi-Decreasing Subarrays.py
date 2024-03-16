class Solution:
    def maxSubarrayLength(self, nums: List[int]) -> int:
        # if i < j, nums[i] > nums[j] and maximum, 
        # no i' < i st. nums[i'] >= nums[i] -> nums[:i+1], nums[i] is largest
        # no j' > j st. nums[j'] <= nums[j] -> nums[j:], nums[j] is smallest
        # all possible i -> monostack, increasing
        # all possible j -> monostack, decreasing
        
        # feasible is
        stacki = []
        for i in range(len(nums)):
            if i == 0 or nums[stacki[-1]] < nums[i]:
                stacki.append(i) 
        
        # start searching j 
        result = 0
        for j in range(len(nums) - 1, -1, -1):
            while stacki and nums[stacki[-1]] > nums[j]:
                result = max(j - stacki.pop() + 1, result)
        
        return result