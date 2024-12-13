class Solution:
    def findScore(self, nums):
        n = len(nums)
        dp = [[nums[i], i] for i in range(n)]

        dp.sort(key=lambda x: x[0])

        marked = [False] * n
        result = 0

        for val, ind in dp:
            if not marked[ind]:
                result += val

                marked[ind] = True
                if ind > 0:
                    marked[ind - 1] = True
                if ind < n - 1:
                    marked[ind + 1] = True

        return result