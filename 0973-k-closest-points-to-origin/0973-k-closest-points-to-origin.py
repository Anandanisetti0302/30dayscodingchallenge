import heapq

class Solution(object):
    def kClosest(self, points, k):
        return heapq.nsmallest(
            k,
            points,
            key=lambda p: p[0] ** 2 + p[1] ** 2
        )
