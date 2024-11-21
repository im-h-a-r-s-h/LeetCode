# LeetCode Problem: 1577-Number-of-Ways-Where-Square-of-Number-Is Equal-to-Product-of-Two-Numbers
# Problem Link: https://leetcode.com/problems/number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers/?envType=problem-list-v2&envId=hash-table
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if len(sentence)<26:
            return False
        a=[0]*26
        for i in sentence:
            a[(ord(i)-97)-1]+=1
        for i in a:
            if i<1:
                return False
        return True
