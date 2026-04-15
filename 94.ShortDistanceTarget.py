def closestTarget(words, target, startIndex):
    n = len(words)
    ans = n
    
    for i, word in enumerate(words):
        if word == target:
            ans = min(ans, abs(i - startIndex), n - abs(i - startIndex))
    
    return ans if ans < n else -1


words = input("Enter words (space separated): ").split()
target = input("Enter target word: ")
startIndex = int(input("Enter start index: "))

# Output
result = closestTarget(words, target, startIndex)
print("Output:", result)

# hello i am abhi hello
# hello
# 1
# -> 1