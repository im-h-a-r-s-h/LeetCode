# LeetCode Problem: 2658-Maximum-Number-of-Fish-in-a-Grid
# Problem Link: https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/
class Solution:
    def numOfFish(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visited or grid[r][c] == 0:
                return 0
            visited.add((r, c))
            fish_count = grid[r][c]
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                fish_count += dfs(r + dr, c + dc)
            return fish_count
        
        max_fish = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 0 and (r, c) not in visited:
                    max_fish = max(max_fish, dfs(r, c))

        return max_fish
