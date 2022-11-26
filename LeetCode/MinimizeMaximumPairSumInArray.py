class Solution:
    def minPairSum(self, nums: List[int]) -> int:

        maxSum = 0
        nums.sort()
        i , j = 0, len(nums) - 1
        while i < j:
            maxSum = max(maxSum, nums[i] + nums[j])
            i += 1
            j -= 1
        return maxSum
