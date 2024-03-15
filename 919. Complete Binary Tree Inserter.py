# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        # construct a complete binary tree
        if root: 
            self.root = root
            self.traverse = [] # bfs traverse
            queue = deque()
            queue.append(root)
            while queue:
                node = queue.popleft()
                self.traverse.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        else:
            self.root = None


    def insert(self, val: int) -> int:
        if not self.root:
            self.root = TreeNode(val)
        else:
            # insert, len + 1 -> knows which is parent
            newNode = TreeNode(val)
            n = len(self.traverse)
            layer = int(math.log2(n+1))
            idx = n  - pow(2, layer) + 1 # starting from 0
            # then parent should be on layer - 1, idx // 2, idx % 2 == 1 -> right

            parentIdx = pow(2, layer - 1) - 1 + idx // 2
            if idx % 2 == 0:
                self.traverse[parentIdx].left = newNode
            else:
                self.traverse[parentIdx].right = newNode
            self.traverse.append(newNode)
            return self.traverse[parentIdx].val


    def get_root(self) -> Optional[TreeNode]:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()