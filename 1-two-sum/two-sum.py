class Solution(object):
    def twoSum(self, nums, target):
        L = {}
        for index , val in enumerate(nums):
            diff = target - val

            if diff in L:
                return [index , L[diff]]
            L[val] = index
         