class Solution:
    def numSpecial(self, mat):
        m, n = len(mat), len(mat[0])
        row = [0] * m
        col = [0] * n

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    row[i] += 1
                    col[j] += 1

        return sum(
            mat[i][j] == 1 and row[i] == 1 and col[j] == 1
            for i in range(m)
            for j in range(n)
        )


# ===== Taking Input from User =====
m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

mat = []

print("Enter the matrix values (0 or 1):")

for i in range(m):
    row = list(map(int, input().split()))
    mat.append(row)

# ===== Calling Function =====
sol = Solution()
result = sol.numSpecial(mat)

print("Number of Special Positions:", result)


# 3
# 3
# 1 0 0
# 0 0 1
# 1 0 0
# -> 1