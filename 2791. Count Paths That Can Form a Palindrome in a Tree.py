class Solution:
    def countPalindromePaths(self, parent: List[int], s: str) -> int:

        n = len(parent)
        children = [[] for _ in range(n)]
        
        for node in range(n):
            if parent[node] == -1:
                continue
            children[parent[node]].append(node)

        masks = [0] * n
        
        # def dfs(node):
        #     #
        #     paths_cur = defaultdict(int)
        #     if not children[node]: # leaf
        #         return {0:1} # mask

        #     # create new mask
        #     numChildren = len(children[node])
        #     paths1 = [defaultdict(int) for _ in range(numChildren)]
        #     for i, cnode in enumerate(children[node]):
        #         paths = dfs(cnode)
        #         index = ord(s[cnode]) - ord('a')
        #         for mask in paths.keys():
        #             new_mask = mask ^ (1 << index)
        #             if new_mask == 0 or ((new_mask & (new_mask - 1)) == 0):
        #                 # print(stNode, node)
        #                 self.result += paths[mask]
        #             paths_cur[new_mask] += paths[mask]
        #             paths1[i][new_mask] += paths[mask]

        #     # calcuate palindrome with right
        #     if numChildren > 1:
        #         for i in range(len(paths1)):
        #             for j in range(i + 1, len(paths1)): # combination
        #                 for m1, c1 in paths1[i].items():
        #                     for m2, c2 in paths1[j].items():
        #                         m = m1 ^ m2
        #                         if m == 0 or ((m & (m - 1)) == 0):
        #                             # print(m, st1, st2)
        #                             self.result += c1 * c2
        #     paths_cur[0] = 1 
        #     return paths_cur

        # dfs(0)
        # return self.result
        def dfs(node, mask): # mask is from root to node 
            # only root to current 
            if node != 0:
                masks[node] = mask ^ (1 << (ord(s[node]) - ord('a')))
            
            for cnode in children[node]:
                dfs(cnode, masks[node])

        dfs(0, 0)
        counter = Counter(masks)
        result = 0

        for i in range(n):
            result += counter[masks[i]]
            result += sum([counter[masks[i] ^ (1 << j)] for j in range(26)])
        
        return (result - n) // 2



