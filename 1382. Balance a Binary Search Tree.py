# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # inorder traversal to find an increasing list
        # using the list construct a  balanced BST. 

        traversal = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            traversal.append(node.val)
            inorder(node.right)

        def constructBST(st, ed):
            if st > ed:
                return None
            if st == ed: # only one 
                node = TreeNode(traversal[st])
                return node
            
            newIdx = (st + ed) // 2
            # find root -> middle
            node = TreeNode(traversal[newIdx])
            leftChild = constructBST(st, newIdx - 1)
            rightChild = constructBST(newIdx + 1, ed)
            node.left = leftChild
            node.right = rightChild
            return node

        inorder(root)
        rootNew = constructBST(0, len(traversal) - 1)

        return rootNew