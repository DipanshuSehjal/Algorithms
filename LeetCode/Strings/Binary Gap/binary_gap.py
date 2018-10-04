"""
Given a positive integer N, find and return the longest distance between two consecutive 1's in the binary representation of N.
If there aren't two consecutive 1's, return 0.

Problem Statement: https://leetcode.com/problems/binary-gap/description/

"""
def binary_gap(n):
    a = '{0:b}'.format(n)
    max_so_far = 0
    curr = 0
    for i in range(len(a)):
        if a[i] == '1':
            j = i+1
            while j < len(a):
                if a[j] == '1':
                    i = j-1
                    curr += 1
                    max_so_far = max(curr, max_so_far)
                    curr = 0
                    break
                else:
                    curr += 1
                    j += 1
    return max_so_far

print((binary_gap(46)))
