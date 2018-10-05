"""
https://leetcode.com/problems/palindromic-substrings/description/

Given a string, your task is to count how many palindromic substrings in this string.
The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.
"""

class Solution:
    def countSubstrings(self, S):
        """
        :type s: str
        :rtype: int
        """
        n = len(S)
        if n == 0 or n == 1:
            return n

        # store the count of PS
        count_PS = [[0 for _ in range(n)] for _ in range(n)]

        # store if str[i..j] is a palindrome substring
        ps = [[False for _ in range(n)] for _ in range(n)]

        # palindrome of single length is 1
        for i in range(n):
            ps[i][i] = True

        for i in range(n-1):
            if S[i] == S[i + 1]:
                ps[i][i + 1] = True
                count_PS[i][i + 1] = 1


        for length in range(2, n):
            for i in range(n-length):
                j = length + i
                if S[i] == S[j] and ps[i+1][j-1]:
                    ps[i][j] = True
                if ps[i][j] == True:
                    count_PS[i][j] = count_PS[i][j - 1] + count_PS[i + 1][j] + 1 - count_PS[i + 1][j - 1]
                else:
                    count_PS[i][j] = count_PS[i][j - 1] + count_PS[i + 1][j] - count_PS[i + 1][j - 1]

        return count_PS[0][n-1] + n