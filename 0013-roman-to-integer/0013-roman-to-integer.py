class Solution:
    def romanToInt(self, s: str) -> int:
        # 'roman numerals': integer values
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        # initialize
        total = 0
        
        for i in range(len(s)):
            # character is smaller than the next
            if i + 1 < len(s) and roman_to_int[s[i]] < roman_to_int[s[i + 1]]:
                total -= roman_to_int[s[i]]
            else:
                total += roman_to_int[s[i]]
        
        return total
