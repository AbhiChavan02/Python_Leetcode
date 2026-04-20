def maxDistance(colors):
    n = len(colors)
    res = 0
    for i in range(n):
        for j in range(i + 1, n):
            if colors[i] != colors[j]:
                res = max(res, j - i)
    return res


colors = list(map(int, input("Enter colors separated by space: ").split()))

print("Output:", maxDistance(colors))

# 1 2 3 1 2
# -> 4