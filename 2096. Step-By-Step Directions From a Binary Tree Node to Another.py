# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # find first node that is both st and ed' parent
        self.result = ""
        self.reach = False
        def dfs(node):
            stRoute = "+"
            edRoute = "+"
            if node.left:
                s, e = dfs(node.left)
                if s != "+":
                    stRoute = s + 'U'
                if e != "+":
                    edRoute = e + 'L'
            if node.right:
                s, e = dfs(node.right)
                if s != "+":
                    stRoute = s + 'U'
                if e != "+":
                    edRoute = e + 'R'
            if node.val == startValue:
                stRoute = ""
            if node.val == destValue:
                edRoute = ""
            if stRoute != "+" and edRoute != "+" and not self.reach:
                self.reach = True
                self.result = stRoute + edRoute[::-1]
            # val1 = str(node.val)
            # print("{} [{}] [{}]".format(val1, stRoute, edRoute))
            return stRoute, edRoute
        dfs(root)
        return self.result

            
        