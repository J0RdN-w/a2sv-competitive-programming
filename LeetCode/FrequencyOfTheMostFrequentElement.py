class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        slow = 0
        for fast in range(len(nums)):
            k += nums[fast]
            if k < nums[fast] * (fast - slow + 1):
                k -= nums[slow]
                slow += 1
        return fast - slow + 1
           
