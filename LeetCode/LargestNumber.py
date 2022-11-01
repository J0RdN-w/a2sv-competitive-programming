class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        num = int(''.join(self.quickSort(nums)))
        return str(num)
    
    def quickSort(self, nums: List[int]):
        if len(nums) <= 1:
            return [str(i) for i in nums]
        pivot = str(nums[0])
        left, right = [], []
        for i in nums[1:]:
            num = str(i)
            if num + pivot <= pivot + num:
                left.append(num)
            else:
                right.append(num)

        return self.quickSort(right) + [pivot] + self.quickSort(left)
