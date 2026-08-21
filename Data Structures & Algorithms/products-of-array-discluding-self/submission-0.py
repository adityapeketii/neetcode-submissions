class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [0]*len(nums)
        suf = [0]*len(nums)

        mul1 = 1
        for i in range(len(nums)):
            pre[i] = mul1
            mul1 *= nums[i]

        mul2 = 1
        for i in range(len(nums)-1, -1, -1):
            suf[i] = mul2
            mul2 *= nums[i]

        return [l*r for l, r in zip(pre, suf)]