class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = collections.deque()
        fresh_count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_count += 1
                elif grid[i][j] == 2:
                    q.append((i, j))

        time = 0

        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q and fresh_count > 0:
            q_size = len(q)
            for i in range(q_size):
                u, v = q.popleft()
                for du, dv in dirs:
                    r = du + u
                    c = dv + v
                    if r in range(m) and c in range(n) and grid[r][c] == 1:
                        fresh_count -= 1
                        grid[r][c] = 2
                        q.append((r, c))

            time += 1

        if fresh_count == 0:
            return time
        return -1
