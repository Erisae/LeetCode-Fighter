class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # only thing to do is remove. 
        stackleft = [] # ( push, ) pop, include their index
        stackright = []
        for idx, c in enumerate(s):
            if c == "(":
                stackleft.append(idx)
            elif c == ")":
                if stackleft:
                    stackleft.pop()
                else: # nothing in left
                    stackright.append(idx)
        # remove everything in stacks
        result = ""
        for idx, c in enumerate(s):
            if idx not in stackleft and idx not in stackright:
                result += c
        return result