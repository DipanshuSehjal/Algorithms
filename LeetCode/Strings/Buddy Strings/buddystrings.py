"""
Given two strings A and B of lowercase letters, return true if and only if we can swap two 
letters in A so that the result equals B

https://leetcode.com/problems/buddy-strings/description/
Easy
"""

class Solution:
    def buddy_strings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False

        flag_start = False
        flag_end = False
        keys = set()
        flag_pair = False
        for i in range(len(A)):
            if A[i] != B[i]:
                if flag_start:
                    if swap_a == B[i] and swap_b == A[i]:
                        flag_end = True
                    else:
                        return False
                else:
                    flag_start = True
                    swap_a = A[i]
                    swap_b = B[i]

            else:
                if A[i] not in keys:
                    keys.add(A[i])
                else:
                    flag_pair = True

        return (flag_end and flag_start) or flag_pair


sol = Solution()
# print(sol.buddyStrings(A="aaaaaaa", B="aaaaaaa"))
print(sol.buddy_strings(A="abbd", B="abbd"))
