class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        queue = deque()
        queue.append((0, 0, 0)) # position and effort. 
        m, n = len(heights), len(heights[0])
        minEffort = [[math.inf for _ in range(n)] for _ in range(m)]
        minEffort[0][0] = 0
        
        while queue:
            # print(queue)
            x, y, maxDiff = queue.popleft() # maxDiff -> maxDiffrence on previous path
            for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
                nx, ny = x + dx, y + dy 
                if 0 <= nx < m and 0 <= ny < n:
                    diff = max(maxDiff, abs(heights[nx][ny] - heights[x][y]))
                    if minEffort[nx][ny] == math.inf or minEffort[nx][ny] > diff:
                        minEffort[nx][ny] = diff 
                        queue.append((nx, ny, minEffort[nx][ny]))
        return minEffort[m-1][n-1]
