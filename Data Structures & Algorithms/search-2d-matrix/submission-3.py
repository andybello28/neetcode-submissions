class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        m = (r + l) // 2
        target_list = None
        while l <= r:
            if target > matrix[m][-1]:
                l = m + 1
                m = (r + l) // 2
            elif target < matrix[m][0]:
                r = m - 1
                m = (r + l) // 2 
            else:
                target_list = m
                break

        if target_list == None:
            return False
        
        l = 0
        r = len(matrix[target_list])
        m = (r + l) // 2

        while l <= r:
            if matrix[target_list][m] == target:
                return True
            elif target > matrix[target_list][m]:
                l = m + 1
                m = (r + l) // 2
            else:
                r = m - 1
                m = (r + l) // 2
        return False

