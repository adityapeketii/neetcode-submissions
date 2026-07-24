class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        counts_n1 = [0]*26
        counts_n2 = [0]*26

        if n1 > n2:
            return False

        for i in range(n1):
            counts_n1[ord(s1[i]) - ord('a')] += 1
            counts_n2[ord(s2[i]) - ord('a')] += 1

        if counts_n1 == counts_n2:
            return True

        for i in range(n1, n2):
            counts_n2[ord(s2[i]) - ord('a')] += 1
            counts_n2[ord(s2[i - n1])- ord('a')] -= 1

            if counts_n1 == counts_n2:
                return True

        return False
        