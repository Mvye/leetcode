class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ind1 = 0
        ind2 = 1
        while ind1 <= len(nums)-1:
            while ind2 <= len(nums)-1:
                if (nums[ind1] + nums[ind2]) == target:
                    return[ind1, ind2]
                ind2 += 1
            ind1 += 1
            ind2 = ind1 + 1
