class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = dict()
        l = s.split()
        if len(l)!=len(pattern):
            return False
        flag=True
        for i in range(len(pattern)):
            if pattern[i] not in d.keys():
                if l[i] not in d.values():
                    d[pattern[i]] = l[i]
                else:
                    flag=False
                    break
            else:
                if d[pattern[i]]!=l[i]:
                    flag=False
                    break

        return flag
