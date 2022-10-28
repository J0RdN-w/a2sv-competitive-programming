class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        products = [1]
        for i in range(1, len(nums)):
            products.append(nums[i-1] * products[-1])
        product = 1
        for i in range(len(nums)-1, -1, -1):
            products[i] *= product
            product *= nums[i]
        return products
            
        
            
        
