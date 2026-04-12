class Solution:
    def minimumDistance(self, word):
        n = len(word)
        BIG = 2**30
        
        dp = [[[BIG] * 26 for _ in range(26)] for _ in range(n)]
        
        # Initial state
        for i in range(26):
            dp[0][i][ord(word[0]) - 65] = 0
            dp[0][ord(word[0]) - 65][i] = 0

        def getDistance(p, q):
            x1, y1 = p // 6, p % 6
            x2, y2 = q // 6, q % 6
            return abs(x1 - x2) + abs(y1 - y2)

        # Fill DP
        for i in range(1, n):
            cur = ord(word[i]) - 65
            prev = ord(word[i - 1]) - 65
            d = getDistance(prev, cur)

            for j in range(26):
                # Move same finger
                dp[i][cur][j] = min(dp[i][cur][j], dp[i - 1][prev][j] + d)
                dp[i][j][cur] = min(dp[i][j][cur], dp[i - 1][j][prev] + d)

                # Try switching finger
                if prev == j:
                    for k in range(26):
                        d0 = getDistance(k, cur)
                        dp[i][cur][j] = min(dp[i][cur][j], dp[i - 1][k][j] + d0)
                        dp[i][j][cur] = min(dp[i][j][cur], dp[i - 1][j][k] + d0)

        ans = min(min(dp[n - 1][x]) for x in range(26))
        return ans


if __name__ == "__main__":
    word = input("Enter word (uppercase letters only): ").strip()
    
    sol = Solution()
    result = sol.minimumDistance(word)
    
    print("Output:", result)


    # CAKE
    # -> 3