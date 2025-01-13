class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        #strip
        s = s.rstrip()
        
        #split
        words = s.split(' ')
        
        #length of the last word
        return len(words[-1]) if words else 0