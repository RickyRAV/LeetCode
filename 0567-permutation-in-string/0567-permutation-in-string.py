class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter = [0] * 26
        s2_counter = [0] * 26

        for ch in s1:
            s1_counter[ord(ch) - ord('a')] += 1
        
        left = 0
        for right in range(len(s2)):
            s2_counter[ord(s2[right]) - ord('a')] += 1
            
            if right - left + 1 > len(s1):
                s2_counter[ord(s2[left]) - ord('a')] -= 1
                left += 1
            
            if s1_counter == s2_counter:
                return True
        
        return False
