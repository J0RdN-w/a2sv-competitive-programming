class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:

        output = []
        for i in range(len(l)):
            subArray = sorted(nums[l[i]: r[i]+1])
            isSeq = True
            for j in range(2, len(subArray)):
                if subArray[0] - subArray[1] != subArray[j-1] - subArray[j]:
                    isSeq = False
            output.append(isSeq)
        return output
