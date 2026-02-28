def concatenatedBinary(n: int) -> int:
    MOD = 10**9 + 7
    res = 0
    bits = 0

    for i in range(1, n + 1):
        # If i is power of 2, increase bit length
        if (i & (i - 1)) == 0:
            bits += 1
        
        res = ((res << bits) | i) % MOD

    return res


# ---- Local Machine Input ----
if __name__ == "__main__":
    n = int(input("Enter value of n: "))
    print("Result:", concatenatedBinary(n))


# 3
# -> 27