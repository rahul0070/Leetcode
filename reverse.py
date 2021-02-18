class Solution:
    def reverseString(self, s):
        n = len(s)//2
        size = len(s)-1
        for i in range(n):
            f = s[i]
            s[i] = s[size-i]
            s[size-i] = f


s= Solution()
s.reverseString(["h","e","l","l","o"])
        