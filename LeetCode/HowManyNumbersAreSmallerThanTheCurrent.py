class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        for i in range(len(nums)):
            for j in nums:
                if nums[i] > j:
                    output[i] += 1
        return output            
        
