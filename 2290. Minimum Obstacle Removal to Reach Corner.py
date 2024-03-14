# class Solution:
#     def minimumObstacles(self, grid: List[List[int]]) -> int:
#         # not moving the obstacle -> removing
#         m, n = len(grid), len(grid[0])
#         minOb = [[math.inf for _ in range(n)] for _ in range(m)]
#         # minOb[i][j]: minimum obstabcles to remove to reach (i, j)
#         pq = []

#         minOb[0][0] = grid[0][0]
#         heapq.heappush(pq, (grid[0][0], 0, 0))

#         while pq:
#             prevDist, i, j = heapq.heappop(pq) # return the current minimum dist with (i, j)
#             for di, dj in zip([0, 0, 1, -1], [1, -1, 0, 0]):
#                 ni, nj = i + di, j + dj
#                 if ni == m - 1 and nj == n - 1: # since using dijkstra, return when first encounter
#                     return prevDist + grid[ni][nj]
#                 if  0 <= ni < m and 0 <= nj < n:
#                     if prevDist + grid[ni][nj] < minOb[ni][nj]: # if resulting a smaller dist for (ni, nj)
#                         minOb[ni][nj] = prevDist + grid[ni][nj]
#                         heapq.heappush(pq, (minOb[ni][nj], ni, nj))

#         return minOb[-1][-1]

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        minOb = [[math.inf for _ in range(n)] for _ in range(m)]
        queue= deque()
        queue.append((grid[0][0], 0, 0))
        while queue:
            prevDist, i, j = queue.popleft()
            for di, dj in zip([0, 0, 1, -1], [1, -1, 0, 0]):
                ni, nj = i + di, j + dj
                if ni == m - 1 and nj == n - 1:
                    return prevDist + grid[-1][-1]
                elif 0 <= ni < m and 0 <= nj < n:
                    if prevDist + grid[ni][nj] < minOb[ni][nj]:
                        minOb[ni][nj] = prevDist + grid[ni][nj]
                        if grid[ni][nj] == 0: 
                        # which means the past path is shorter than when grid[ni][nj] == 1
                        # should be handled first -> like mimPath dijkstra
                            queue.appendleft((minOb[ni][nj], ni, nj)) # would be handled first
                        else:
                            queue.append((minOb[ni][nj], ni, nj))
        return minOb[-1][-1]



        
