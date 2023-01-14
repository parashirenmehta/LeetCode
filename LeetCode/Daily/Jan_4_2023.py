from collections import Counter
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        d = dict(Counter(tasks))
        vals = list(d.values())
        vals.sort(reverse=True)

        if 1 in vals:
            return -1

        rounds = 0
        for v in vals:
            if v%3==1:
                rounds+= v//3+1
            else:
                rounds+= v//3+(v%3)//2

        return rounds
