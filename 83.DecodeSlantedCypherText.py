class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if rows == 1:
            return encodedText

        n = len(encodedText)
        cols = n // rows
        res = []

        for c in range(cols):
            r, j = 0, c
            while r < rows and j < cols:
                res.append(encodedText[r * cols + j])
                r += 1
                j += 1

        return "".join(res).rstrip()


if __name__ == "__main__":
    encodedText = input("Enter encoded text: ")
    rows = int(input("Enter number of rows: "))

    sol = Solution()
    result = sol.decodeCiphertext(encodedText, rows)

    print("Decoded text:", result)

    # ch   ie   pr
    # 3
    # -> cipher