class NumArray(object):
    def __init__(self, nums):
        self.prefix_sums = [0]
        for num in nums:
            self.prefix_sums.append(self.prefix_sums[-1] + num)

    def sumRange(self, left, right):
        return self.prefix_sums[right + 1] - self.prefix_sums[left]
