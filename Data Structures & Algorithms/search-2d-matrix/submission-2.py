class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #Binary search
        l = 0
        r = len(matrix)*len(matrix[0]) - 1
        m = len(matrix)
        n = len(matrix[0])
        while l <= r:
            m = (l+r) // 2
            i, j = m//n, m % n

            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                l = m + 1
            else:
                r = m - 1
            
        return False