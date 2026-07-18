class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr = ""
        for c in s:
            if c.isalnum():
                newstr += c.lower()

        rev = newstr[::-1]
        if newstr == rev:
            return True
        return False
        