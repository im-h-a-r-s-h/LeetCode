Problem Name: 1399-Count-Largest-Group
Problem Link: https://leetcode.com/problems/count-largest-group/description/?envType=problem-list-v2&envId=hash-table&difficulty=EASY

class Solution:
    def countLargestGroup(self, n: int) -> int:
        def count(n):
            sumi=0
            while(n>0):
                sumi+=n%10
                n=n//10
            return sumi
        d={}
        ans=0
        for i in range(1,n+1):
            key=count(i)
            if key in d:
                d[key]+=1
            else:
                d[key]=1
        k=max(d.values())
        for i,j in d.items():
            if j==k:
                ans+=1
        return ans

# Complexity
- Time complexity:O(N)
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:O(N)
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
