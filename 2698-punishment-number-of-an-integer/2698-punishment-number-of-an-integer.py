class Solution:
    def punishmentNumber(self, n: int) -> int:
        def isPos(j,s,i,curr):
            if j==len(s):
                return curr==i
            for index in range(j,len(s)):
                val=int(s[j:index+1])
                if isPos(index+1,s,i,curr+val):
                    return True
            return False

        res=0
        for i in range(n+1):
            if isPos(0,str(i*i),i,0):
                res+=i*i
        return res
