import heapq


class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """
        current = []
        feature = sorted(zip(capital, profits))[::-1]
        for _ in range(k):
            while feature and feature[-1][0] <= w:
                heapq.heappush(current, -feature.pop()[1])
            if current:
                w -= heapq.heappop(current)
        return w
