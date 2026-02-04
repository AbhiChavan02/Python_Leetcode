class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        curr_row = 0
        going_down = False

        for ch in s:
            rows[curr_row] += ch

            if curr_row == 0 or curr_row == numRows - 1:
                going_down = not going_down

            curr_row += 1 if going_down else -1

        return "".join(rows)


# -------- local input/output --------
if __name__ == "__main__":
    s = input("Enter string: ")
    numRows = int(input("Enter number of rows: "))

    sol = Solution()
    result = sol.convert(s, numRows)

    print("Output:", result)


    # PAYPALISHIRING
    # 3
    # -> PAHNAPLSIIGYIR
