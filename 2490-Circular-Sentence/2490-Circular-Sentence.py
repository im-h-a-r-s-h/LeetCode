# LeetCode Problem: 2490-Circular-Sentence
# Problem Link: https://leetcode.com/problems/circular-sentence/description/

# Approach 1: Using linear complexity
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        temp=sentence[0]
        if sentence[0]!=sentence[-1]:
            return False
        for i in range(len(sentence)):
            if sentence[i]==" ":
                if sentence[i+1]==" ":
                    continue
                if sentence[i+1]!=temp:
                    return False
            else:
                temp=sentence[i]
        return True
            
        
