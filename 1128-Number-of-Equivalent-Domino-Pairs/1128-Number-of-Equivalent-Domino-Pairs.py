# LeetCode Problem: 1128-Number-of-Equivalent-Domino-Pairs
# Problem Link: https://leetcode.com/problems/number-of-equivalent-domino-pairs/solutions/5999292/simple-solution-two-approaches/

# Approach 1: Using hashmap
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        d={}
        cnt=0
        for i,j in dominoes:
            key=(min(i,j),max(i,j))
            if key in d:
                cnt += d[key]
                d[key]+=1
            else:
                d[key]=1
        return cnt

# Approach 2: Using Bruteforce
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        cnt=0
        for i in range(len(dominoes)-1):
            s1=dominoes[i][0]
            s2=dominoes[i][1]
            for j in range(i+1,len(dominoes)):
                d1=dominoes[j][0]
                d2=dominoes[j][1]
                if (s1==d1 and s2==d2) or (s1==d2 and s2==d1):
                    cnt+=1
        return cnt
