class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        rows = [''] * numRows
        curRow, step = 0, -1
        for ch in s:
            rows[curRow] += ch
            if curRow == 0 or curRow == numRows - 1:
                step = -step
            curRow += step
        return ''.join(rows)


        