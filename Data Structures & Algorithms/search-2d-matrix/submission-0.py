class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        dims = rows * cols

        l = 0
        r = dims - 1

        while l <= r: 
            mid = (l + r) // 2
            
            val = matrix[mid // cols][mid % cols]
            if target == val: return True

            if target > val: l = mid + 1
            else: r = mid - 1
        
        return False

