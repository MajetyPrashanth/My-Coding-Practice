class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i in range(len(nums)):
            temp = nums[i]
            rem = target - temp
            if rem in d.keys():
                return [d[rem], i]
            d[nums[i]] = i
