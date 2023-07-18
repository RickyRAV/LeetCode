class Solution:
    def romanToInt(self, s: str) -> int:
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        prev = 0
        #reverse iteration
        for i in s[::-1]:
            curr = rom_val[i]
            if prev > curr:
                int_val -= curr
            else:
                int_val += curr
                prev = curr
        return int_val