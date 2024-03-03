class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # counter -> the number of each capital letter in the window
        # when maxValue + k >= len(window) -> says that maxValue's character can take place of the whole window
            # -> right move to expand window
        # when not -> can not take place window
            # -> left move to shrink window
        
        left, right = 0, 0
        counter = [0] * 26
        counter[ord(s[right]) - ord('A')] = 1

        n = len(s)
        maxWin = 1
        while left < n and right < n:
            if max(counter) + k >= right - left + 1:
                maxWin = max(maxWin, right - left + 1)
                right += 1
                if right >= n:
                    break
                counter[ord(s[right]) - ord('A')] += 1
            else:
                left += 1
                counter[ord(s[left - 1]) - ord('A')] -= 1
        
        return maxWin



