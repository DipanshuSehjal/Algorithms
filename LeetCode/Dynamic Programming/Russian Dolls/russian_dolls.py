"""
https://leetcode.com/problems/russian-doll-envelopes/description/

You have a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit 
into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.
What is the maximum number of envelopes can you Russian doll? (put one inside other)

A variant of Longest increasing subsequence. O(nlogn)
"""

from operator import itemgetter

class Solution:

    def max_envelopes(self, envelopes):
        
        # sort the list by width([0]) in increasing order and then sort the heights in non-decreasing order
        # with in the subarray of same widths
        envelopes.sort(key=lambda sl: (sl[0], -sl[1]))
        
        tails=[]
        for (w,h) in envelopes:
            idx=bisect.bisect_left(tails, h)
            if idx==len(tails):
                tails.append(h)                        
            elif idx==0 or tails[idx-1]<h:
                tails[idx]=h
        return len(tails)   
