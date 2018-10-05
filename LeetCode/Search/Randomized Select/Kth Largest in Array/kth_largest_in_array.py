"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
"""

from random import randrange

class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # tweak: k-th largest
        return self.r_select(nums, len(nums)-k)

    def partition(self, x, pivot_index=0):
        i = 0
        if pivot_index != 0: x[0], x[pivot_index] = x[pivot_index], x[0]
        for j in range(len(x) - 1):
            if x[j + 1] < x[0]:
                x[j + 1], x[i + 1] = x[i + 1], x[j + 1]
                i += 1
        x[0], x[i] = x[i], x[0]
        return x, i

    def r_select(self, x, k):

        if len(x) == 1:
            return x[0]
        else:
            xpart = self.partition(x, randrange(len(x)))
            x = xpart[0]  # partitioned array
            j = xpart[1]  # pivot index
            if j == k:
                return x[j]
            elif j > k:
                return self.r_select(x[:j], k)
            else:
                k = k - j - 1
                return self.r_select(x[(j + 1):], k)

