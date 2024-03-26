class Solution:
    # def nextGreaterElements(self, nums: List[int]) -> List[int]:
    #     # bruteforce, search later and search front
    #     n = len(nums)
    #     result = []
    #     def lookFoward(i, num): # curernt index and nums
    #         for j in range(i + 1, n):
    #             if nums[j] > num:
    #                 return j 
    #         return -1

    #     def lookFront(i, num):
    #         for j in range(i):
    #             if nums[j] > num:
    #                 return j
    #         return -1

    #     for i, num in enumerate(nums):
    #         j = lookFoward(i, num)
    #         if j != -1: # exist in later
    #             result.append(nums[j])
    #         else:
    #             j = lookFront(i, num)
    #             if j == -1:
    #                 result.append(-1)
    #             else:
    #                 result.append(nums[j])
    #     return result

    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        n = len(nums)
        result = [-1 for _ in range(n)]
        for j in range(2):
            for i in range(n - 1, -1, -1):
                if not stack:
                    stack.append(i)
                elif nums[i] < nums[stack[-1]]: # push and update
                    result[i] = nums[stack[-1]]
                    stack.append(i)
                else: # pop until is <
                    while stack and nums[i] >= nums[stack[-1]]:
                        stack.pop()
                    if stack:
                        result[i] = nums[stack[-1]]
                    stack.append(i)
        return result


