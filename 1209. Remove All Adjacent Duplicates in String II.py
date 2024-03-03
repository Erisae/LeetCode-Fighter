# class Solution:
#     def removeDuplicates(self, s: str, k: int) -> str:
#         idx = 0
#         while idx < len(s):
#             if idx + k - 1 < len(s) and s[idx:idx+k] == s[idx]*k: # remove
#                 s_temp = s[:idx] + s[idx+k:]
#                 s = s_temp
#                 if idx > 0:
#                     idx -= 1
#                 while idx - 1 >= 0 and s[idx] == s[idx-1]:
#                     idx -= 1
#             else: # increment
#                 idx += 1
        
#         return s


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            stack.append(c)
            if len(stack) >= k and stack[-k:] == [stack[-1]]*k: # same
                stack = stack[:-k].copy()
        
        return ''.join(stack)
