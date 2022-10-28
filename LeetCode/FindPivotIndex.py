class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        l_sum, r_sum = 0, sum(nums)
        
        for indx, num in enumerate(nums):
            r_sum -= num
            if l_sum == r_sum:
                return indx
            l_sum += num
        return -1
