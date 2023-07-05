class Solution(object):
    def longestSubarray(self, nums):

        deleted = 0
        result = 0
        if 0 not in nums:
            return len(nums)-1
        else:
            while deleted < len(nums):
                deleted += 1
                count = 0
                k = 0
                if nums[deleted - 1] == 1:
                    continue
                else:
                    for i in nums:

                        if k == (deleted-1):
                            k += 1
                            continue
                        if i == 1:
                            count += 1
                        if i == 0:
                            k+=1
                            count = 0
                            continue
                        
                        if count > result:
                            result = count
                        k += 1


        return result

object = Solution()
nums= []
if 1 > len(nums) and len(nums) > 10 ** 5:
    raise Exception("input must in between 1 and 10 to the power of 5")
object.longestSubarray(nums)
