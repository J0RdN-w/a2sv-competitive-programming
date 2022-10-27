class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:

        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]


        res, Lmax, Mmax = nums[firstLen + secondLen - 1], nums[firstLen - 1], nums[secondLen - 1]


        for i in range(firstLen + secondLen, len(nums)):
            Lmax = max(Lmax, nums[i - secondLen] - nums[i - firstLen - secondLen])
            res = max(res, Lmax + nums[i] - nums[i - secondLen])

        for i in range(firstLen + secondLen, len(nums)):
            Mmax = max(Mmax, nums[i - firstLen] - nums[i - firstLen - secondLen])
            res = max(res, Mmax + nums[i] - nums[i - firstLen])

        return res
        
