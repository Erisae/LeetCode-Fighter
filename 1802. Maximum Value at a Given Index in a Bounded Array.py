class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def constructMinSum(value): # construct minimal sum when index's value is value
            # 1, 1, 1, 2, .., value-1, value, value-1, ... 2, 1
            sum = value
            # left
            if index - (value - 1) < 0: # not reaching 1 on left
                if index > 0:
                    sum += (value - 1 - (index - 1) + value - 1) * index / 2
            else: # reaching 1 on left
                if index > 0:
                    sum += index - (value - 1) - 1 + 1
                    sum += (1 + value - 1)*(value - 1) / 2
            # right
            if index + value - 1 >= n: # not reaching 1 on right
                if index < n - 1:
                    sum += (value - 1 + value - 1 - (n - 1 - (index + 1))) * (n - 1 - (index + 1) + 1) / 2
            else:
                if index < n - 1:
                    sum += n - 1 - (index + value - 1 + 1) + 1
                    sum += (1 + value - 1)*(value - 1) / 2
            # print(value, sum)
            return int(sum)

        # binary search
        left = 1
        right = maxSum
        while left <= right:
            mid = (left + right) // 2
            if constructMinSum(mid) <= maxSum:
                left = mid + 1
            else:
                right = mid - 1
        return left - 1