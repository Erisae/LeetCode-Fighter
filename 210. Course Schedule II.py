class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # toposort, dfs reach the furthest and append to visited
        # return the reverse of visited

        visited = []
        
        # edge
        edge = defaultdict(list)
        for prereq in prerequisites:
            edge[prereq[1]].append(prereq[0])

        def dfs(node, rec_stack = []):
            if node in rec_stack:
                return False
            rec_stack.append(node)
            for nextNode in edge[node]:
                if not nextNode in visited:
                    if not dfs(nextNode, rec_stack):
                        return False
            visited.append(node)
            rec_stack.remove(node)
            del edge[node]
            return True
        
        # do dfs 
        for course in range(numCourses):
            if not course in visited:
                if not dfs(course, []):
                    return []
        
        return visited[::-1]
        