# class Solution:
#     def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
#         self.timeMax = 0

#         nextCourse = defaultdict(list)
#         for r in relations:
#             nextCourse[r[0] - 1].append(r[1] - 1)

#         @cache
#         def dfs(node): # dfs, record the maximum time used along the way
#             if not nextCourse[node]: # reached an end
#                 return time[node]
            
#             ans = 0
#             for newNode in nextCourse[node]:
#                 ans = max(ans, dfs(newNode))
#             return ans + time[node]

#         res = 0
#         for i in range(n):
#             res = max(dfs(i), res)
        
#         return res

class Solution:
    def minimumTime(self, n, relations, time):
        # topo sort

        # construct graph and indegree
        indegree = [0] * n
        graph = defaultdict(list)
        for prev, nxt in relations:
            graph[prev - 1].append(nxt - 1)
            indegree[nxt - 1] += 1

        # construct queue and do bfs
        queue = deque()
        maxRoute = 0
        dist = 0
        maxPrev = [0] * n

        # queue initilization
        for idx, inde in enumerate(indegree):
            if inde == 0: # not explored and dependencies all met
                queue.append(idx)

        while queue:
            # pop and proceed
            node = queue.popleft() # arrive at node

            # calculate maxRoutee
            if not graph[node]:
                maxRoute = max(maxRoute, maxPrev[node] + time[node])

            # new indegree and enqueue
            for nxt in graph[node]:
                indegree[nxt] -= 1
                maxPrev[nxt] = max(maxPrev[nxt], maxPrev[node] + time[node])
                if indegree[nxt] == 0:
                    queue.append(nxt)
        return maxRoute

            





        
