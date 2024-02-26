class Solution:
    def minJumps(self, arr: List[int]) -> int:

        # base
        if len(arr) == 1:
            return 0
        # grouping by number
        group = defaultdict(list)
        for idx, value in enumerate(arr):
            group[value].append(idx)

        # bfs starting from the first index
        queue = deque()
        queue.append((0, 0)) # index and distance
        visited = [False] * len(arr)
        visited[0] = True
        while queue:
            idx, dist = queue.popleft()
            # find next

            # initializate candidates as all indices that has value arr[idx] - idx
            candidates = group[arr[idx]].copy()
            if idx in candidates:
                candidates.remove(idx)

            # remove in group, to avoid over-calculation
            group[arr[idx]] = []

            # include idx - 1 and idx + 1
            if idx - 1 >= 0:
                candidates.append(idx - 1)
            if idx + 1 < len(arr):
                candidates.append(idx + 1)

            # early stop and enqueue unvisited candidates
            for candidate in candidates:
                if candidate == len(arr) - 1: # last one
                    return dist + 1
                if not visited[candidate]:
                    visited[candidate] = True
                    queue.append((candidate, dist + 1))
        return -1

            
