import numpy as np
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        ngas = np.array(gas)
        ncost = np.array(cost)

        diff = list(ngas-ncost)
        if sum(diff)<0:
            return -1
        
        stack = []
        stackans = 0
        i=0
        while i<len(diff):
            if diff[i]>=0:
                stack.append([diff[i],i])
                stackans+=diff[i]
            else:
                if stackans+diff[i]>=0:
                    stack.append([diff[i],i])
                    stackans+=diff[i]
                else:
                    stackans=0
                    stack=[]
            i+=1

        return stack[0][1]
