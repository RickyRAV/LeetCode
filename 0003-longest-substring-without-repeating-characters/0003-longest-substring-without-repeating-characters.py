class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        longest_length = start = 0
        
        for end in range(len(s)):
            while s[end] in chars:
                chars.remove(s[start])
                start += 1
            chars.add(s[end])
            longest_length = max(longest_length, end - start + 1)
            
        return longest_length