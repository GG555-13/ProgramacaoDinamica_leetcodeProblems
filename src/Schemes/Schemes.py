from typing import List

class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        m = len(group)
        dp = [[[0] * (minProfit + 1) for _ in range(n + 1)] for _ in range(m + 1)]       
        dp[0][0][0] = 1

        for i in range(1, m + 1):  
            members = group[i - 1] 
            earn = profit[i - 1]    
            for j in range(n + 1):  
                for k in range(minProfit + 1): 
                    dp[i][j][k] = dp[i - 1][j][k]   
                    if j >= members:
                        dp[i][j][k] += dp[i - 1][j - members][max(0, k - earn)]
                    
                    
        mod = 10**9 + 7
        dp[i][j][k] %= mod
        result = sum(dp[m][j][minProfit] for j in range(n + 1)) % mod
        return result

def teste():
    solution = Solution()
    
    ct = [
        (5, 3, [2, 2], [2, 3], 2),  
        (10, 5, [2, 3, 5], [6, 7, 8], 7),  
        (1, 1, [1], [1], 1),  
        (5, 10, [2, 2, 3], [1, 2, 3], 0), 
        (100, 50, [10, 20, 30], [20, 30, 40], 0)  
    ]
    
    for i, (n, minProfit, group, profit, expected) in enumerate(ct):
        result = solution.profitableSchemes(n, minProfit, group, profit)
        print(f"Test case {i + 1}: n = {n}, minProfit = {minProfit}, group = {group}, profit = {profit}")
        print(f"Result: {result}")
        print(f"Expected: {expected}\n")

if __name__ == "__main__":
    teste()
