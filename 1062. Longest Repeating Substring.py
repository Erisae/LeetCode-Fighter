class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        # objective is longest -> not repeat at most times -> should at least repeat once is ok
        # length not more than n // 2, length not less than 2
        # one side rule exist -> if len=k has duplicate -> len=k-1 must have duplicate, then search up

        n = len(s)
        if n < 3:
            return 0
        left = 2
        right = n - 1
        while left <= right:
            print(left, right)
            searchRight = False
            mid = (left + right) // 2
            # take mid as the test substring length
            for i in range(n - mid + 1): # substring starts with i 
                if s[i:i+mid] in s[i+1:]: # exist 
                    searchRight = True
                    break
            if searchRight:
                left = mid + 1
            else:
                right = mid - 1
        if left == 2:
            return 0
        return left - 1

