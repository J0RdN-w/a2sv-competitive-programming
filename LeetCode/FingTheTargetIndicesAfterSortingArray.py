class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        
        output = []
        
        for i in range(len(nums)):
            min_indx = i
            for j in range(i+1, len(nums)):
                if nums[j] < nums[min_indx]:
                    min_indx = j
            (nums[i], nums[min_indx]) = (nums[min_indx], nums[i]) 
            if nums[i] == target:
                output.append(i)
                
        return output       
               
