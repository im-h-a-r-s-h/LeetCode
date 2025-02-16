# LeetCode Problem: 1071. Greatest Common Divisor of Strings
# Problem Link: https://leetcode.com/problems/greatest-common-divisor-of-strings/

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if(str1+str2!=str2+str1):
            return ""
        def gcd(a,b):
            if b==0:
                return a
            return gcd(b,a%b)
        return str1[0:gcd(len(str1),len(str2))]
