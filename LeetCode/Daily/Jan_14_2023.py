class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        n=len(s1)
        adj = dict()

        for i in range(n):
            if s1[i] in adj.keys():
                adj[s1[i]].append(s2[i])
            else:
                adj[s1[i]] = [s2[i]]
            if s2[i] in adj.keys():
                adj[s2[i]].append(s1[i])
            else:
                adj[s2[i]] = [s1[i]]

        visited=dict()
        t = list(adj.keys())
        for el in t:
            visited[el]=False
            
        nodes = len(list(adj.keys()))
        
        def dfs(curr,parent,l,visited):
            
            if visited[curr]==True:
                return l
            l.append(curr)
            visited[curr]=True
            
            for child in adj[curr]:
                if child==parent:
                    continue
                if visited[child]==True:
                    continue
                l = dfs(child,curr,l,visited)

            return l

        ll = []
        keyslist = list(adj.keys())
        while keyslist!=[]:
            l = dfs(keyslist[0],'',[],visited)
            for k in l:
                keyslist.remove(k)
            ll.append(l)

        finald = dict()
        minl = []
        for templ in ll:
            tl = min(templ)
            for el in templ:
                finald[el]=tl

        finals = ""
        for c in baseStr:
            if c in finald.keys():
                finals+=finald[c]
            else:
                finals+=c

        return finals
