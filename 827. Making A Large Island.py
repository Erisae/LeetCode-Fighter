class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        # can know the size of each island
        # can only switch 0 that has 1 next to it
        # save the index of each of island, when comes to 0, check neighbor

        sizes = []

        m = len(grid)
        n = len(grid[0])

        def dfs(x, y, index):
            grid[x][y] = index
            res = 1
            for dx, dy in zip([1, -1, 0, 0], [0, 0, 1, -1]):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                    res += dfs(nx, ny, index)
            return res

        def neighborSum(x, y):
            neighbor = set()
            for dx, dy in zip([1, -1, 0, 0], [0, 0, 1, -1]):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != 0:
                    neighbor.add(grid[nx][ny])
            res = 0
            for nb in list(neighbor):
                res += sizes[nb - 2]
            return res

        result = 0
        
        index = 2
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    sizes.append(dfs(i, j, index))
                    result = max(result, sizes[-1])
                    index += 1
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0: # 
                    result = max(result, neighborSum(i, j) + 1)

        return result

                