class Solution:
    def search(self, arr, target):
        low = 0
        high = len(arr)-1
        while(low <= high):
            mid = low + (high - low) // 2
            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
    

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            if self.search(matrix[i], target):
               return True
        return False