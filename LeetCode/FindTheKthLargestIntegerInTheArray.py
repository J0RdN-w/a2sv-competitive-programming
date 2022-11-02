class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        
        '''
        solution 2: since each elements might not fit the integer limit in other language
        i used mergesort with string
        '''
        def mergeSort(nums):
            if len(nums) <= 1:
                return nums
            
            mid = len(nums) // 2
            left = mergeSort(nums[:mid])
            right = mergeSort(nums[mid:])
            return merge(left, right)
        
        def merge(left, right):
            i, j, nums = 0, 0, []
            while i < len(left) and j < len(right):
                if len(left[i]) < len(right[j]):
                    nums.append(left[i])
                    i += 1
                elif len(left[i]) > len(right[j]):
                    nums.append(right[j])
                    j += 1
                else:
                    if left[i] <= right[j]:
                        nums.append(left[i])
                        i += 1
                    else:
                        nums.append(right[j])
                        j += 1
            nums.extend(left[i:])
            nums.extend(right[j:])
            return nums
        
        return mergeSort(nums)[-k]
    
        # solution 1: 
        return sorted(nums, key=lambda num: int(num))[-k]
        
