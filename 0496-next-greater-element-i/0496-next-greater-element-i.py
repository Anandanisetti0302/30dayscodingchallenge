class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        nxt = {}
        for num in nums2:
            while stack and stack[-1] < num:
                nxt[stack.pop()] = num
            stack.append(num)
        return [nxt.get(num, -1) for num in nums1]

        