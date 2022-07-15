class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        maxi = 0

        def search(rc):
            val = 0
            if grid[rc[0]][rc[1]] == 1:
                grid[rc[0]][rc[1]] = 0
                val += 1
                if rc[0] > 0:
                    val += search([rc[0] - 1, rc[1]])
                if rc[0] < row - 1:
                    val += search([rc[0] + 1, rc[1]])
                if rc[1] > 0:
                    val += search([rc[0], rc[1] - 1])
                if rc[1] < col - 1:
                    val += search([rc[0], rc[1] + 1])
            return val

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    maxi = max(maxi, search([r, c]))
        return maxi
