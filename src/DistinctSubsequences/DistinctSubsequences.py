class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)        
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = 1
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j]
        
        return dp[m][n]

def teste():
    solution = Solution()
    
    ct = [
        ("rabbbit", "rabbit", 3),  
        ("babgbag", "bag", 5), 
        ("", "a", 0), 
        ("abc", "", 1),  
        ("aabb", "ab", 4),  
        ("abcde", "ace", 1)  
    ]
    
    for i, (s, t, expected) in enumerate(ct):
        result = solution.numDistinct(s, t)
        print(f"Test case {i + 1}: s = {s}, t = {t}")
        print(f"Result: {result}")
        print(f"Expected: {expected}\n")

if __name__ == "__main__":
    teste()
