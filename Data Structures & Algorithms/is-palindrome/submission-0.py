class Solution:
    def isPalindrome(self, s: str) -> bool:
        defstr = ""
        for c in s:
            if c.isalnum():
                defstr += c.lower()
        return defstr == defstr[::-1]
