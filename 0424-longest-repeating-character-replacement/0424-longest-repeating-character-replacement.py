class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        max_len = max_count = start = 0
        
        for end in range(len(s)):
            count[ord(s[end]) - ord('A')] += 1
            max_count = max(max_count, count[ord(s[end]) - ord('A')])
            if end - start + 1 - max_count > k:
                count[ord(s[start]) - ord('A')] -= 1
                start += 1
            max_len = max(max_len, end - start + 1)
        return max_len