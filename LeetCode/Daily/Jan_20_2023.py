class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        ans =[]
        n = len(nums)
        for i in range(n):
            tlist = [row[:] for row in ans]
            for j in range(len(ans)):
                if nums[i]>=ans[j][-1]:
                    tlist[j].append(nums[i])
            
            for item in tlist:
                if item not in ans:
                    ans.append(item)
            #ans.extend(tlist)
            ans.append([nums[i]])
        i=0
        while i<len(nums):
            if [nums[i]] in ans:  
                ans.remove([nums[i]])
            i+=1

        return ans
