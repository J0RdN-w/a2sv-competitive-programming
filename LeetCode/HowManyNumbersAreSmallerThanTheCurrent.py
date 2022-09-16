class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        output = []
        data = dict(zip(sorted(nums), range(len(nums))))
        
        
        for i in nums:
            output.append(data.get(i) - (nums.count(i) - 1))
        
        return output   
