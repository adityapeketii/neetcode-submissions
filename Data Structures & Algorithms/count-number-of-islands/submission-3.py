class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        num_islands = 0

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == "0":
                return
            else:
                grid[i][j] = "0"
                dfs(i, j+1)
                dfs(i, j-1)
                dfs(i+1, j)
                dfs(i-1, j)     

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    num_islands += 1
                    dfs(i, j)

        return num_islands

        # seen = set()

        # def bfs(i, j):
        #     q = collections.deque()
        #     q.append((i, j))
        #     seen.add((i, j))

        #     while q:
        #         r, c = q.popleft()
        #         dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        #         for dr, dc in dirs:
        #             a, b = r + dr, c + dc
        #             if (a >= 0 and a < m 
        #             and b >= 0 and b < n
        #             and grid[a][b] == "1" and (a, b) not in seen):
        #                 seen.add((a, b))
        #                 q.append((a, b))

        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == "1" and (i, j) not in seen:
        #             num_islands += 1
        #             bfs(i, j)

        # return num_islands
        