class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, slow, fast = len(nums), 0, 1
        if l <= 1:
            return 
        else:
            while fast < l:
                if nums[slow] == 0 and nums[fast] != 0:
                    nums[slow], nums[fast] = nums[fast], nums[slow]
                    slow, fast = slow + 1, fast + 1
                elif nums[slow] == 0 and nums[fast] == 0:
                    fast += 1
                else:
                    slow, fast = slow + 1, fast + 1
                    
