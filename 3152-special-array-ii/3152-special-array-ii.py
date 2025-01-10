class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        #track breaks 
        breaks = [0] * n
        
        #mark breaks 
        for i in range(1, n):
            if (nums[i] % 2) == (nums[i-1] % 2):
                breaks[i] = 1
        
        #cumulative breaks
        for i in range(1, n):
            breaks[i] += breaks[i-1]
        
        #queries
        result = []
        for fromi, toi in queries:
            #it's special
            result.append(breaks[toi] - breaks[fromi] == 0)
        
        return result