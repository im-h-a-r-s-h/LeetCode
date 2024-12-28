# LeetCode Problem: 1487-Making-File-Names-Unique
# Problem Link: https://leetcode.com/problems/making-file-names-unique/description/
class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        res = []
        d = {}
        for i in names:
            if i not in d:
                d[i] = 0
                res.append(i)
            else:
                d[i] += 1
                new_name = f"{i}({d[i]})"
                while new_name in d:
                    d[i] += 1
                    new_name = f"{i}({d[i]})"
                d[new_name] = 0
                res.append(new_name)
        return res
