class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        l = sorted(points, key=lambda item:item[1])
        stack = []
        ans=0

        i=0
        while i<len(l):
            stack.append(l[i])
            j=i+1
            while j<len(l) and l[j][0]<=stack[0][1]:
                stack.append(l[j])
                j+=1
                
            ans+=1
            stack = []
            i=j
            
        return ans
