class Solution(object):
    def permuteUnique(self, nums):
        nums.sort()
        res = []
        used = [False] * len(nums)
        def backtrack(path):
            if len(path) == len(nums):
                res.append(list(path))
                return
            for i in range(len(nums)):
                if used[i] or (i > 0 and nums[i] == nums[i-1] and not used[i-1]):
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack(path)
                path.pop()
                used[i] = False
        backtrack([])
        return res

        