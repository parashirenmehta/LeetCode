class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        adj = {i:[] for i in range(n)}

        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        def dfs(curr, parent,d,l):
            d = {}
            for child in adj[curr]:
                if child==parent:
                    continue
                d1,l = dfs(child, curr,d,l)
                for k in d1.keys():
                    if k in d.keys():
                        d[k]+=d1[k]
                    else:
                        d[k]=d1[k]
            if labels[curr] not in d.keys():
                d[labels[curr]]=1
            else:
                d[labels[curr]]+=1
            l[curr] = d[labels[curr]]
            return d,l

        d,l = dfs(0,-1,dict(),[0 for i in range(n)])
        return l
