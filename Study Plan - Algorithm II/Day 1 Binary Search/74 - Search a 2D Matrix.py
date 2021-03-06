class Solution:
    def searchMatrix(
            self,
            matrix: List[List[int]],
            target: int) -> bool:  # 90.37% 33.09%
        left, right = 0, len(matrix) * len(matrix[0]) - 1
        while left <= right:
            mid = left + (right - left) // 2
            row, col = divmod(mid, len(matrix[0]))
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                right = mid - 1
            elif matrix[row][col] < target:
                left = mid + 1
        return False
