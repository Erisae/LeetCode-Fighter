class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        # 0001111
        counter = Counter(s)
        preZero = 0 # not including this
        sufOne = counter['1'] # not including this
        if s[0] == '1':
            sufOne -= 1
        n = len(s)
        result = n
        for i in range(n):
            result = min(result, i - preZero + n - i - 1 - sufOne)
            if s[i] == '0':
                preZero += 1
            if i + 1 < n and s[i+1] == '1':
                sufOne -= 1
        
        return result