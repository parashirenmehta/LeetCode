class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = {i:[] for i in range(n)}

        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        def dfs(curr,parent):
            time=0
            for neighbour in adj[curr]:
                if neighbour==parent:
                    continue
                neighbourTime = dfs(neighbour, curr)

                if neighbourTime or hasApple[neighbour]:
                    time+= 2+neighbourTime

            return time

        return dfs(0,-1)
