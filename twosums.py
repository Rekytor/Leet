class Solution(object):
    def twoSum(self, nums, target):
        i=0
        while i<len(nums):
            for j in range(i+1,len(nums)):
                if nums[j]+nums[i]==target:
                    return i,j
            i+=1



object = Solution()
nums = [2,7,11,15]
target = 9
object.twoSum(nums,target)