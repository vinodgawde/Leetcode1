class Solution:
    def max_ele(self, mat, n, m, mid):
        max_val = float('-inf')
        ind = 0
        for i in range(n):
            if mat[i][mid] > max_val:
                max_val = mat[i][mid]
                ind = i
        return ind

    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])
        low = 0
        high = m - 1
        while(low <= high):
            mid = low + (high - low) // 2
            max_row = self.max_ele(mat, n, m, mid)
            left = mat[max_row][mid - 1] if mid - 1 >= 0 else -1
            right = mat[max_row][mid + 1] if mid + 1 < m else -1

            if mat[max_row][mid] > left and mat[max_row][mid] > right:
                return  [max_row, mid]
            elif mat[max_row][mid] < left:
                high = mid - 1
            else:
                low = mid + 1
        
        return [-1, -1]
