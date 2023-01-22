def isValid(s):
    l = s.split(".")
    if '' in l:
        return False
    for item in l:
        if len(item)!=len(str(int(item))):
            return False
        if int(item)>=0 and int(item)<=255:
            continue
        else:
            return False
    return True

def traverse(s,dots,ans):
    if dots==3:
        if isValid(s):
            ans.append(s)
        return ans
    if dots==0:
        ans = traverse(s[0]+"."+s[1:],dots+1,ans)
        ans = traverse(s[:2]+"."+s[2:],dots+1,ans)
        ans = traverse(s[:3]+"."+s[3:],dots+1,ans)

        return ans

    if dots==1:
        index = s.index('.')
        ans = traverse(s[:index+2]+"."+s[index+2:],dots+1,ans)
        ans = traverse(s[:index+3]+"."+s[index+3:],dots+1,ans)
        ans = traverse(s[:index+4]+"."+s[index+4:],dots+1,ans)

        return ans

    if dots==2:
        index = s.find('.',s.find('.')+1)
        ans = traverse(s[:index+2]+"."+s[index+2:],dots+1,ans)
        ans = traverse(s[:index+3]+"."+s[index+3:],dots+1,ans)
        ans = traverse(s[:index+4]+"."+s[index+4:],dots+1,ans)

        return ans

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        return traverse(s,0,[])
