class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        t = [[0] * (n + 1) for _ in range(m + 1)]

        # Compute LCS table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    t[i][j] = 1 + t[i - 1][j - 1]
                else:
                    t[i][j] = max(t[i - 1][j], t[i][j - 1])

        # Backtrack to build the shortest common supersequence
        i, j = m, n
        scs = []

        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:  # If characters match, include only once
                scs.append(str1[i - 1])
                i -= 1
                j -= 1
            elif t[i - 1][j] > t[i][j - 1]:  # Move towards the larger value
                scs.append(str1[i - 1])
                i -= 1
            else:
                scs.append(str2[j - 1])
                j -= 1

        # Add remaining characters from both strings
        while i > 0:
            scs.append(str1[i - 1])
            i -= 1
        while j > 0:
            scs.append(str2[j - 1])
            j -= 1

        return "".join(reversed(scs))
