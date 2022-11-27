class Solution:
    def minSetSize(self, arr: List[int]) -> int:

        hashMap = {}
        for each in arr:
            hashMap[each] = hashMap.get(each, 0) + 1
        count = sorted(hashMap.values(), reverse=True)
        res, s = 0, 0
        while s < len(arr) / 2:
            s += count[res]
            res += 1
        return res
