class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        result = 0
        # instead of insert ( -> insert accumulative score, eg: 1, 2, 4
        for c in s:
            if c == '(':
                stack.append(1)
            else: # is ), a pair
                top = stack.pop()
                if stack:
                    if stack[-1] == 1: # first time
                        stack[-1] = top * 2
                    else:
                        stack[-1] += top * 2
                else:
                    result += top
        return result