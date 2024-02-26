class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        # bfs with (idx, dist, credit), credit -> number of obstacles that can be eleminated
        # original bfs -> only consider unvisited, this one -> if visit with larger credit, then enqueue again
        # so visited -> max credit on this grid

        m, n = len(grid), len(grid[0])

        # base
        if m == 1 and n == 1:
            return 0

        queue = deque()
        queue.append(((0, 0), 0, k))
        visited = [[-1 for _ in range(n)] for _ in range(m)]
        visited[0][0] = k

        while queue:
            (x, y), dist, credit = queue.popleft()
            new_dist = dist + 1
            new_credit = credit
            for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
                nx = x + dx
                ny = y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    # if is obstacle
                    if grid[nx][ny] == 1:
                        new_credit = credit - 1
                    else:
                        new_credit = credit
                    # if is destination
                    if nx == m - 1 and ny == n - 1 and new_credit >= 0:
                        return new_dist
                    
                    # since initialization is -1, when credit <= -1 would not be enqueue
                    if new_credit > visited[nx][ny]:
                        visited[nx][ny] = new_credit
                        queue.append(((nx, ny), new_dist, new_credit))
        print(visited)
        return -1

