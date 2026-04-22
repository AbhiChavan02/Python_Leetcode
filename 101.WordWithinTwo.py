class Solution:
    def twoEditWords(self, queries, dictionary):
        ans = []
        for query in queries:
            for s in dictionary:
                dis = 0
                for i in range(len(query)):
                    if query[i] != s[i]:
                        dis += 1
                if dis <= 2:
                    ans.append(query)
                    break
        return ans


queries = input("Enter queries (space-separated): ").split()
dictionary = input("Enter dictionary words (space-separated): ").split()
sol = Solution()
result = sol.twoEditWords(queries, dictionary)
print("Output:", result)


# word note wood
# ward note wood
# -> ['word', 'note', 'wood']