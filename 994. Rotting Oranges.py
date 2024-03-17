class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # bfs, with time, and multiple start. 
        queue = deque()
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j, 0)) # location and time

        maxTime = 0
        while queue:
            x, y, t = queue.popleft()
            maxTime = max(maxTime, t)
            for dx, dy in zip([0, 0, -1, 1], [-1, 1, 0, 0]):
                nx, ny = x + dx, y + dy 
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1: # can be affected
                    queue.append((nx, ny, t + 1))
                    grid[nx][ny] = 2
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return maxTime
            
