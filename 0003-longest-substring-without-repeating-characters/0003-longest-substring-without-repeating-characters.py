class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        set_chars = set()
        
        ans = i = j = 0
        while i < n and j < n:
            if s[j] not in set_chars:
                set_chars.add(s[j])
                j += 1
                ans = max(ans, j - i)
                
            else:
                set_chars.remove(s[i])
                i += 1
        return ans