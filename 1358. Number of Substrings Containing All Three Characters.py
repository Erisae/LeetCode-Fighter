class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # 2 ptr, at 0
        # if not enough -> move right
        # if enough -> move left

        left, right = 0, 0
        n = len(s) 
        counter = defaultdict(int)
        counter[s[0]] += 1
        
        def satisfy(counter):
            cand = ['a', 'b', 'c']
            for c in cand:
                if counter[c] < 1:
                    return False
            return True

        res = 0
        while left < n or right < n:
            if satisfy(counter): # if satisfy, shrink by moving left, but all including [left, right] should be acceptable
                res += n - right
                left += 1
                counter[s[left-1]] -= 1
            else:
                right += 1
                if right == n:
                    break
                counter[s[right]] += 1
        return res
                
