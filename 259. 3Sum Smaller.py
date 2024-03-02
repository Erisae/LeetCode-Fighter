class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:

        n = len(nums)
        if n < 3:
            return 0

        # sort the nums
        nums.sort()

        # fix first, and then 2 ptr
        fix_ptr = 0
        result = 0
        old = 0
        while fix_ptr + 2 < n:
            left = fix_ptr + 1
            right = n - 1
            while left < right:
                if nums[left] + nums[right] + nums[fix_ptr] < target: # good
                    result += right - left # means fix left, and all right ok
                    left += 1 # move left
                else:
                    if nums[left] + nums[int(right / 2)] + nums[fix_ptr] >= target: # directly
                        right = int(right / 2) # or will not pass
                    else:
                        right = right - 1
                    
                    
            fix_ptr += 1
        
        return result


        