# class Solution:
#     def removeStones(self, stones: List[List[int]]) -> int:
#         # heap, first remove least shared
#         xs = defaultdict(int)
#         ys = defaultdict(int)
#         for x, y in stones:
#             xs[x] += 1
#             ys[y] += 1
        
#         def findMinSum(xs, ys):
#             minSum = math.inf
#             minX = -1
#             minY = -1
#             for x, y in stones:
#                 if (xs[x] > 1 or ys[y] > 1) and xs[x] + ys[y] < minSum:
#                     minSum = xs[x] + ys[y]
#                     minX, minY = x, y
#             return minX, minY

#         result = 0
        
#         while True:
#             x, y = findMinSum(xs, ys)          
#             if x < 0: # only it self
#                 break
#             # delete x, y
#             xs[x] -= 1
#             ys[y] -= 1
#             result += 1
#             stones.remove([x, y])
#             print(x, y)
#         return result

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]  # Each element is its own root initially
        self.size = [1 for i in range(size)]

    def find(self, x):
        """Finds the root of the set that element x belongs to."""
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])  # Path compression
        return self.root[x]

    def union(self, x, y):
        """Unites the sets that elements x and y belong to."""
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            self.root[rootY] = rootX
            self.size[rootX] += self.size[rootY]
    


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # union when has same array or axis
        nstones = len(stones)
        uf = UnionFind(nstones)
        for i in range(nstones):
            for j in range(i + 1, nstones):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    uf.union(i, j)
        
        # each size - 1
        res = 0
        visited = []
        for i in range(nstones):
            root = uf.find(i)
            if root not in visited:
                res += uf.size[root] - 1
                visited.append(root)
        return res

            

