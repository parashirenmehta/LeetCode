class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        rows = len(strs[0])
        cols = len(strs)
        count = 0

        for j in range(rows):
            m = strs[0][j]
            for i in range(cols):
                if strs[i][j]>=m:
                    m = strs[i][j]
                else:
                    count+=1
                    break
        
        return count
