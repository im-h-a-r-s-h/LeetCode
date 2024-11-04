# LeetCode Problem: 3163-String-Compression-III
# Problem Link: https://leetcode.com/problems/string-compression-iii/description/
class Solution:
    def compressedString(self, word: str) -> str:
        temp=[1]
        temp.append(word[0])
        ind=0
        for i in range(1,len(word)):
            if word[i]==word[i-1]:
                if temp[ind]==9:
                    temp.append(1)
                    temp.append(word[i])
                    ind+=2
                else:
                    temp[ind]+=1
            else:
                temp.append(1)
                temp.append(word[i])
                ind+=2
        ans=""
        for i in temp:
            ans+=str(i)
        return ans

        
