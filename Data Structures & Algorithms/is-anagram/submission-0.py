class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n1 = len(s)
        n2 = len(t)

        if n1 != n2:
            return False

        dict_1 = defaultdict(int)
        dict_2 = defaultdict(int)

        for ch_1, ch_2 in zip(s, t):
            dict_1[ch_1] += 1
            dict_2[ch_2] += 1

        if dict_1 == dict_2:
            return True

        return False
        