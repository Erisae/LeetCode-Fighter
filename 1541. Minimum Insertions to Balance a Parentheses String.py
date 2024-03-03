class Solution:
    def minInsertions(self, s: str) -> int:
        # most importantly, two conseductive )) is viewed as a valid closing point
        unpaired_start = 0
        idx = 0
        n = len(s)
        result = 0
        while idx < n:
            if s[idx] == '(':
                unpaired_start += 1
                idx += 1
            else: # is )
                if not unpaired_start: # no ( on stack
                    if s[idx:idx+2] == '))': # insert a (
                        result += 1
                        idx += 2
                    else: #
                        result += 2 # insert ( and )
                        idx += 1
                else: # has ( on stack
                    if s[idx:idx+2] == '))': # close and pop
                        unpaired_start -= 1
                        idx += 2
                    else: 
                        result += 1 # insert )
                        unpaired_start -= 1
                        idx += 1
        result += unpaired_start * 2

        return result
    
                
