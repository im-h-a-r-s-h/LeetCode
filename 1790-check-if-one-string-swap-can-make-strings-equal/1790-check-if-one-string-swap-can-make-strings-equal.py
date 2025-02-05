# LeetCode Problem: 1790. Check if One String Swap Can Make Strings Equal
# Problem Link: https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/


#APPROACH 1:

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        n = len(s1)
        cnt = 0
        si = -1
        sj = -1
        for i in range(n):
            if s1[i] != s2[i] and si == -1:
                si = i
                cnt += 1
            elif s1[i] != s2[i] and si != -1:
                cnt += 1
                sj = i
        if cnt == 0 or (cnt == 2 and s1[si] == s2[sj] and s2[si] == s1[sj]):
            return True
        else:
            return False

# APPROACH 2: BRUTEFORCE

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1==s2:
            return True
        for i in range(len(s2)):
            for j in range(i+1,len(s2)):
                temp=list(s2)
                temp[i],temp[j]=temp[j],temp[i]
                print(''.join(temp),s1)
                if ''.join(temp)==s1:
                    return True
        return False
            
        
