class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        self.timeMax = 0

        nextCourse = defaultdict(list)
        for r in relations:
            nextCourse[r[0] - 1].append(r[1] - 1)

        @cache
        def dfs(node): # dfs, record the maximum time used along the way
            if not nextCourse[node]: # reached an end
                return time[node]
            
            ans = 0
            for newNode in nextCourse[node]:
                ans = max(ans, dfs(newNode))
            return ans + time[node]

        res = 0
        for i in range(n):
            res = max(dfs(i), res)
        
        return res