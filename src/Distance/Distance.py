class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(m + 1):
            dp[i][0] = i  
        for j in range(n + 1):
            dp[0][j] = j
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                        dp[i - 1][j] + 1, #deletar    
                        dp[i][j - 1] + 1, #inserir    
                        dp[i - 1][j - 1] + 1 #substituir 
                    )
        return dp[m][n]
    

def teste():
    solution = Solution()
    
    ct = [
        ("horse", "ros", 3),  
        ("intention", "execution", 5), 
        ("", "", 0),
        ("abc", "abc", 0),  
        ("abc", "", 3), 
        ("", "abc", 3),  
        ("abcdef", "azced", 3)  
    ]
    
    for i, (word1, word2, expected) in enumerate(ct):
        result = solution.minDistance(word1, word2)
        print(f"Test case {i + 1}: word1 = {word1}, word2 = {word2}")
        print(f"Result: {result}")
        print(f"Expected: {expected}\n")

if __name__ == "__main__":
    teste()
