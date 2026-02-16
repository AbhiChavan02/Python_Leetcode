class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0

        for _ in range(32):
            result <<= 1
            result |= (n & 1)
            n >>= 1

        return result


if __name__ == "__main__":
    n = int(input("Enter a number: "))
    
    sol = Solution()
    answer = sol.reverseBits(n)
    
    print("Reversed bits integer:", answer)


# 43261596
# -> 964176192