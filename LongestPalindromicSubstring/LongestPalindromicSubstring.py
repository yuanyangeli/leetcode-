class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        f, l = 0, len(s)
        #特殊情况特殊处理（字符串为空或者字符串中的字符相同）
        if l == 0 or s.count(s[0]) == l:
            return (s)
        else:
            for i in range(l):
                #回文串的结束条件是 现有回文串的长度大于l/2 并且i的长度也大于l/2
                if f >= l / 2 and i > l / 2:
                    break
                for j in range(i, l + 1):
                    if f <= abs(i - j) and s[i:j] == s[i:j][::-1]:
                        rslt = s[i:j]
                        f = abs(i - j)
        return (rslt)
