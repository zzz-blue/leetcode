class Solution:
    def search(self, nums, target):
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[hi] and nums[hi] < target:
                hi = mid - 1
            elif target < nums[lo] and nums[mid] >= nums[lo]:
                lo = mid + 1
            else:
                if target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
        return -1

    def searchInsert(self, nums, target):
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo

    def isValidSudoku(self, board):
        valid_row = [[True] * 9 for i in range(9)]
        valid_column = [[True] * 9 for i in range(9)]
        valid_cell = [[True] * 9 for i in range(9)]
        for i in range(9):
            for j in range(9):
                value = (board[i][j])
                if value != '.':
                    value = int(value) - 1
                    cell_index = (i // 3) * 3 + (j // 3)
                    if valid_row[i][value] and valid_column[j][value] and valid_cell[cell_index][value]:
                        valid_row[i][value], valid_column[j][value], valid_cell[cell_index][value] \
                            = False, False, False
                    else:
                        return False
        return True

    def solveSudoku(self, board):
        valid_row = [[True] * 9 for i in range(9)]
        valid_column = [[True] * 9 for i in range(9)]
        valid_cell = [[True] * 9 for i in range(9)]
        for i in range(9):
            for j in range(9):
                value = (board[i][j])
                if value != '.':
                    value = int(value) - 1
                    cell_index = (i // 3) * 3 + (j // 3)
                    valid_row[i][value], valid_column[j][value], valid_cell[cell_index][value] = False, False, False

        def back_trace(i, j):
            if i == 9:
                return True
            if board[i][j] != '.':
                return back_trace(i + (j + 1) // 9, (j + 1) % 9)
            for value in range(9):
                cell_index = (i // 3) * 3 + (j // 3)
                if valid_row[i][value] and valid_column[j][value] and valid_cell[cell_index][value]:
                    board[i][j] = str(value + 1)
                    valid_row[i][value], valid_column[j][value], valid_cell[cell_index][value] = False, False, False
                    if back_trace(i + (j + 1) // 9, (j + 1) % 9):
                        return True
                    valid_row[i][value], valid_column[j][value], valid_cell[cell_index][value] = True, True, True
                    board[i][j] = '.'
            return False

        back_trace(0, 0)


if __name__ == "__main__":
    solution = Solution()
    board = [[".", ".", ".", ".", ".", ".", ".", "1", "2"], [".", ".", ".", ".", "3", "5", ".", ".", "."],
             [".", ".", ".", "6", ".", ".", ".", "7", "."], ["7", ".", ".", ".", ".", ".", "3", ".", "."],
             [".", ".", ".", "4", ".", ".", "8", ".", "."], ["1", ".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", "1", "2", ".", ".", ".", "."], [".", "8", ".", ".", ".", ".", ".", "4", "."],
             [".", "5", ".", ".", ".", ".", "6", ".", "."]]
    solution.solveSudoku(board)
    print(board)
