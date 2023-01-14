class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        if len(points)==1:
            return 1
        mainans = []
        for i in range(len(points)):
            x1,y1 = points[i][0],points[i][1]
            j = i+1
            d = dict()
            while j<len(points):
                x2,y2 = points[j][0],points[j][1]
                    
                slope = (y2-y1)/(x2-x1) if (x2-x1)!=0 else float('inf')
                if slope not in d.keys():
                    d[slope] = 1
                else:
                    d[slope]+=1
                j+=1
            
            if d=={}:
                continue
            mainans.append(max(list(d.values())))

        return max(mainans)+1
