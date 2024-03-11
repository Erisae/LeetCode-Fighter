class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # omg, the original problem asked on March 4th, 2024
        # Recursion, at least K -> whole -> if counter[a] < K in all -> does not include a, split on a
        # left of a / right of a 
        if k == 1:
            return len(s)
        self.maxLen = 0
        def findBelowK(st, ed):
            if st >= ed:
                return
            counter = Counter(s[st : ed + 1])
            splits = [char for char, v in counter.items() if v < k ]
            if not splits:
                self.maxLen = max(self.maxLen, ed - st + 1)
                return

            nxt = st
            for i in range(st, ed + 1):
                if s[i] in splits:
                    findBelowK(nxt, i - 1)
                    nxt = i + 1
            if nxt != st:
                findBelowK(nxt, ed)

        findBelowK(0, len(s) - 1)
        return self.maxLen
                    
                