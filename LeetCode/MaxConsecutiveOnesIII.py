class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # ans, n = 0, len(nums)
        # for i in range(n):
        #     j = i
        #     z = 0
        #     while j < n and (nums[j] == 1 or z < k):
        #         if nums[j] == 0:
        #             z += 1
        #         j += 1
        #     ans = max(ans, j-i)
        # return ans
        left = right = 0
      
        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1
            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
      
        return right - left + 1
