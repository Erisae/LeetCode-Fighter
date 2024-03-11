class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # dijkstra which is bfs, maintain a credit on every node visited, when comes with a higher credit can search again
        
        # compute edges
        graph = defaultdict(list) # to, price
        for f in flights:
            graph[f[0]].append(f[1:])
        
        # bfs initialization
        queue = deque()
        visited = dict()

        queue.append([src, k + 1, 0]) # node / credit / cost
        visited[src] = [k + 1, 0] # stores max credit and min cost

        result = sys.maxsize

        while queue:
            prevNode, prevCredit, prevCost = queue.popleft()
            if prevCredit == 0: # stops here
                continue
            # for out going edges
            for [node, cost] in graph[prevNode]:
                if node == dst: # destination
                    result = min(result, prevCost + cost)
                if node not in visited.keys(): # not visited
                    queue.append([node, prevCredit - 1, prevCost + cost])
                    visited[node] = [prevCredit - 1, prevCost + cost]
                elif visited[node][0] < prevCredit - 1: # more credit
                    queue.append([node, prevCredit - 1, prevCost + cost])
                    visited[node][0] = prevCredit - 1
                elif visited[node][1] >  prevCost + cost: # less cost
                    queue.append([node, prevCredit - 1, prevCost + cost])
                    visited[node][1] = prevCost + cost
        
        if result == sys.maxsize:
            return -1
        else:
            return result