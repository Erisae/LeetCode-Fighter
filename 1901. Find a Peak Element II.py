class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        # -> binary search
        # not find all -> just find one. 
        # split -> first find a column -> in that column find a row that is maximized -> left and right

        m, n = len(mat), len(mat[0])

        def findMaxInColumn(column):
            maxVal = -1
            maxIdx = -1
            for i in range(m):
                if mat[i][column] > maxVal:
                    maxVal = mat[i][column]
                    maxIdx = i
            return maxIdx

        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            rowId = findMaxInColumn(mid)
            
            # compare with left and right neighbors
            l = mid - 1
            r = mid + 1
            largerL, largerR = False, False
            if (0 <= l < n and mat[rowId][l] < mat[rowId][mid]) or (l < 0):
                largerL = True
            if (0 <= r < n and mat[rowId][r] < mat[rowId][mid]) or (r > n - 1):
                largerR = True
            if largerL and largerR:
                return [rowId, mid]
            elif not largerL:
                right = mid - 1
            else:
                left = mid + 1


