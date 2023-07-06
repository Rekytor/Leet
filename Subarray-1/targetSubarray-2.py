import sys
class Solution(object):

    def minSubArrayLen(self, target, nums):
        INT_MIN = -sys.maxsize - 1
        max_sum = INT_MIN
        n,i = 0,0
        while i <len(nums):
            if 1 > nums[i] and nums[i] > 10 ** 4:
                raise Exception("input must in between 1 and 10 to the power of 4")
            i+=1
        if len(nums) == 2:
            if nums[0] + nums[1] >= target:
                return 2

        if len(nums) == 1:
            if nums[0] >= target:
                return 1
            else:
                return 0

        while n <= len(nums):
            j = 0
            while j < len(nums):
                elementnum = n
                add = 0
                while elementnum >= 0 and j+n < len(nums):
                    add += nums[j-elementnum+n]
                    if add >= target:
                        result = n+1
                        return result
                    elementnum -= 1
                j += 1
            n += 1
        return 0

object = Solution()
nums = [2,3,1,2,4,3]
target = 7
if 1 >= target and len(nums) > 10 ** 9:
    raise Exception("target must in between 1 and 10 to the power of 9")
if 1 > len(nums) and len(nums) > 10 ** 5:
    raise Exception("array length must in between 1 and 10 to the power of 5")

object.minSubArrayLen(target,nums)
