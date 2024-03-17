# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        # each node has a subtree -> should save when traversed, also save a count. 
        result = []
        result_val = []
        visited = []
        def dfs(node): # return list of traversal, past order 
            if not node:
                return [None]
            leftSub = dfs(node.left)
            rightSub = dfs(node.right)
            # compose res
            res = leftSub.copy() + rightSub.copy()
            res.append(node)

            # compose value
            vals = [] 
            for n in res:
                if n:
                    vals.append(n.val)
                else:
                    vals.append("a")

            if vals in visited and vals not in result_val:
                result.append(node)
                result_val.append(vals.copy())
            elif vals not in visited:
                visited.append(vals.copy())

            return res
        
        dfs(root)
        return result