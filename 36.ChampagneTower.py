class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:

        dp = [[0.0] * (r + 1) for r in range(query_row + 1)]
        dp[0][0] = poured
        
        for r in range(query_row):
            for c in range(len(dp[r])):
                if dp[r][c] > 1:
                    overflow = (dp[r][c] - 1) / 2.0
                    dp[r + 1][c] += overflow
                    dp[r + 1][c + 1] += overflow
        
        return min(1, dp[query_row][query_glass])

if __name__ == "__main__":
    poured = int(input("Enter poured amount: "))
    query_row = int(input("Enter query row: "))
    query_glass = int(input("Enter query glass: "))
    
    sol = Solution()
    result = sol.champagneTower(poured, query_row, query_glass)
    
    print("Answer:", result)


# 2
# 1
# 1
# -> 0.5