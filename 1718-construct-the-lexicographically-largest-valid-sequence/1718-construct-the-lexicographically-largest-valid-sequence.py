# LeetCode Problem: 1718. Construct the Lexicographically Largest Valid Sequence
# Problem Link: https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        def solve(index, count, ans, used):
            if count == n:
                return True
            if ans[index] != 0:
                return solve(index + 1, count, ans, used)
            for i in range(n, 0, -1):
                if i in used:
                    continue 
                if i == 1:
                    ans[index] = 1
                    used.add(1)
                    if solve(index + 1, count + 1, ans, used):
                        return True
                    ans[index] = 0
                    used.remove(1)
                else:
                    second_pos = index + i
                    if second_pos < size and ans[second_pos] == 0:
                        ans[index] = ans[second_pos] = i
                        used.add(i)
                        if solve(index + 1, count + 1, ans, used):
                            return True
                        ans[index] = ans[second_pos] = 0
                        used.remove(i)
            return False

        size = 2 * n - 1
        ans = [0] * size 
        used = set() 
        solve(0, 0, ans, used)
        return ans
