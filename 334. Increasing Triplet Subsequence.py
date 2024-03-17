class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # O(n) time complexity and O(1) space complexity
        smallest = math.inf
        second_smallest = math.inf

        for num in nums:
            if num <= smallest: 
                smallest = num
            elif num <= second_smallest:
                second_smallest = num
            else: # find the one that is bigger then first 2 
                return True
        return False
        