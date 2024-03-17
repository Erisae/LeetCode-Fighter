class Solution:
    def maximumSwap(self, num: int) -> int:
        # find digit that is not maximum, swap
        s = list(str(num))
        sorted_s = sorted(s, reverse=True) 
        idx = 0
        while idx < len(s) and s[idx] == sorted_s[idx]:
            idx += 1
        if idx >= len(s):
            return num
        # find last one in s that equals sorted_s[idx]
        for i in range(len(s) - 1, idx, -1):
            if s[i] == sorted_s[idx]:
                print(i, idx)
                s[i], s[idx] = s[idx], s[i]
                break
        
        return int("".join(s))
