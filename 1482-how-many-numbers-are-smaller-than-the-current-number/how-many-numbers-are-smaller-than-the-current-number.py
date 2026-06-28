class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        temp = sorted(nums)
        d = {}
        for i, val in enumerate(temp):
            if val not in d:
                d[val] = i
        ret = []
        for n in nums:
            ret.append(d[n])
        return ret
     
               