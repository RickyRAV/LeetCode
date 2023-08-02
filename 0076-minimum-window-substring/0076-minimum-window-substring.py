from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        dict_t = Counter(t)

        required = len(dict_t)

        # Initialize two pointers 
        l, r = 0, 0

        # formed is used to keep track of how many unique characters in t are present in the current window in its desired frequency.
        formed = 0

        # Dictionary which keeps a count of all the unique characters in the current window.
        window_counts = {}

        # Result list [window length, left, right]
        ans = float("inf"), None, None

        while r < len(s):

            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1

            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1

            while l <= r and formed == required:
                character = s[l]

                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1

                l += 1    

            r += 1    
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]
