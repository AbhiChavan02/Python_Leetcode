class Solution:
    def reverse(self, n: int) -> int:
        res = 0
        while n > 0:
            res = res * 10 + n % 10
            n //= 10
        return res

    def mirrorDistance(self, n: int) -> int:
        return abs(n - self.reverse(n))


if __name__ == "__main__":
    n = int(input("Enter a number: "))

    sol = Solution()
    result = sol.mirrorDistance(n)

    print("Mirror Distance:", result)


    # 123
    # -> 198