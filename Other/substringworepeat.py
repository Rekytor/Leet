import sys
INT_MIN = -sys.maxsize - 1
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        max_sum = INT_MIN

        i=0
        my_data = []
        if len(s)==0:
            return 0
        elif s[0]==" " and len(s)==1:
            return 1
        if len(s)==1:
            return 1
        while i<len(s):
            if s[i] not in my_data:
                my_data.append(s[i])
            else:
                try:
                    filtered_data = list(filter(lambda x: s[i] in x, my_data))
                    if filtered_data:
                        index = my_data.index(filtered_data[0])
                        del my_data[:index + 1]
                except ValueError:
                    pass
                my_data.append(s[i])
            i+=1
            max_sum = max(len(my_data), max_sum)
        print(max_sum)
        return max_sum

s = "dvdf"
if 0 > len(s) and len(s) > 5*10 ** 4:
    raise Exception("array length must in between 1 and 10 to the power of 5")
object = Solution()
object.lengthOfLongestSubstring(s)