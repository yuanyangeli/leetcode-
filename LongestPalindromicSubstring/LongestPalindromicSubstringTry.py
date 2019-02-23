class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        tag = 0
        string = ''
        if len(s) == 1:
            return s
        for i in range(len(s)):
            for j in range(i,len(s)):
                tag = 0
                ss = s[i:j+1]
                for k in range(0,int(len(ss)/2)):
                    if ss[k] == ss[len(ss) - k - 1]:
                        continue
                    else:
                        tag = 1
                        break
                if tag == 0:
                    string = ss if len(ss) >= len(string) else string
        return string
