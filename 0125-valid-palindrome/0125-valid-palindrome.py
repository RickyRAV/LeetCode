class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        while left < right:
            #if characters are alphanumeric
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            else:
                #compare chars, case-insensitive
                if s[left].lower() != s[right].lower():
                    return False
                left, right = left + 1, right - 1
        return True
        