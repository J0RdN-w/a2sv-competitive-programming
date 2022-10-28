class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        # total count, sum of contigous subarray and prefix sum with base case of 0
        count, currSum, prfxSum, = 0, 0, {0: 1}
        
        for num in nums:
            currSum += num 
            
            # check if difference of k and current sum exist in prfxSum and update count if exist
            diff = currSum - k
            count += prfxSum.get(diff, 0)
            
            # adding the current sum to the prfxSum
            prfxSum[currSum] = 1 + prfxSum.get(currSum, 0)
        return count
            
                
        
        
