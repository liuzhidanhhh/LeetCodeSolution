# DP求解
class Solution:
    def minDistance(self, word1, word2):
        n = len(word1)
        m = len(word2)
        dist = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(m + 1):
            dist[0][i] = i
        for j in range(n + 1):
            dist[j][0] = j
        for i in range(n):
            for j in range(m):
                if word1[i] == word2[j]:
                    dist[i+1][j+1] = 1 + min((dist[i][j]-1), dist[i+1][j], dist[i][j+1])
                else:
                    dist[i+1][j+1] = 1 + min(dist[i][j], dist[i+1][j], dist[i][j+1])
        return dist[n][m]


if __name__ == '__main__':
    # word1 = "horse"
    # word2 = "ros"
    word1 = "intention"
    word2 = "execution"
    solve = Solution()
    res = solve.minDistance(word1, word2)
    print(res)
