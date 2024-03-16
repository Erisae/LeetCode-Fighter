class Solution:
    def nextGreaterElement(self, n: int) -> int:
        s = list(str(n)) # convert to string
        len1 = len(s)
        # find the last decreasing subsequence
        firstIdx = -1 # firstIdx that is not in the decreasing subseq
        for i in range(len1 - 1, 0, -1): # i is index 
            if not s[i] <= s[i-1]:
                firstIdx = i - 1
                break
        if firstIdx == -1: # which means all sequence is decreasing, no bigger
            return -1

        # find the first one that is bigger than s[firstIdx]
        swapIdx = 0
        for i in range(len1 - 1, firstIdx, -1):
            if s[i] > s[firstIdx]:
                swapIdx = i
                break
        
        # swap and sort increasing
        s[swapIdx], s[firstIdx] = s[firstIdx], s[swapIdx]
        s[firstIdx+1:] = sorted(s[firstIdx+1:])
        
        # compare with int32
        res = int("".join(s))
        maxInt32 = 2**31 - 1
        if res > maxInt32:
            return -1
        return res
        