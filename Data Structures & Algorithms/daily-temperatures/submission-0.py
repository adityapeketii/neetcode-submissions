class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = temperatures
        n = len(temps)
        res = [0]*n
        stack = []

        for i, t in enumerate(temps):
            while stack and stack[-1][0] < t:
                res_t, res_i = stack.pop()
                res[res_i] = i - res_i
            stack.append((t, i))

        return res

        