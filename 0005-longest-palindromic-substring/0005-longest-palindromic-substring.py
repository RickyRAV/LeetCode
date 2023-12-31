class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        ans = ""
        
        #check substrings of string
        for l in range(n):
            for i in range(n):
                j = i + l
                if j >= len(s):
                    break
                    
                #single char is palindrome
                if l == 0:
                    dp[i][j] = True
                    
                #two same chars form palindrome
                elif l == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (dp[i+1][j-1] and s[i] == s[j])
                    
                #update ans
                if dp[i][j] and l + 1 > len(ans):
                    ans = s[i:j+1]
                    
        return ans