class unionFind:
    def __init__(self, num):
        self.parent = [i for i in range(num)]
        self.size = [1 for _ in range(num)]

    def union(self, num1, num2):
        root1 = self.find(num1)
        root2 = self.find(num2)

        if root1 != root2:
            self.parent[root2] = root1
            self.size[root1] += self.size[root2]

    def find(self, num):
        if self.parent[num] != num:
            self.parent[num] = self.find(self.parent[num])
        return self.parent[num]


class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        # create adjacency list
        adjacency = defaultdict(list)
        for edge in edges:
            adjacency[edge[0]].append(edge[1])
            adjacency[edge[1]].append(edge[0])
        
        # create value -> index list
        sameVal = defaultdict(list)
        for idx, val in enumerate(vals):
            sameVal[val].append(idx)

        # iterate over val, from small to large (union neighbor if < curernt, so when val, all < val connected)
        sorted_val = sorted(sameVal.keys())

        uf = unionFind(len(vals))
        result = 0
        for val in sorted_val:
            for idx in sameVal[val]:
                for neighbor in adjacency[idx]:
                    if vals[neighbor] <= vals[idx]:
                        uf.union(idx, neighbor)
            
            # after merging the idx of same value
            roots = defaultdict(int) # root -> count
            for idx in sameVal[val]:
                roots[uf.find(idx)] += 1
            for count in roots.values():
                result += int(count * (count + 1) / 2)
        
        return result
