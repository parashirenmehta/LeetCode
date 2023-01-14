class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:

        n = len(parent)
        adj = {i:[] for i in range(n)}

        for i in range(1,n):
            adj[i].append(parent[i])
            adj[parent[i]].append(i)

        ans = [1 for i in range(n)]
        
        def dfs(curr,parent,s):
            childlongestpath = []
            for child in adj[curr]:
                if child==parent:
                    continue
                childpath = dfs(child,curr,s)
                if s[child]!=s[curr]:
                    childlongestpath.append(childpath)
            
            childlongestpath.sort(reverse=True)
            if len(childlongestpath)==1:
                ans[curr] = 1+childlongestpath[0]
                return ans[curr]
            
            if len(childlongestpath)>1:
                ans[curr] = 1+childlongestpath[0]+childlongestpath[1]
                return 1+childlongestpath[0]
            
            return 1
        
        l = dfs(0,-1,s)
        return max(ans)
