from typing import List
from collections import Set

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = set()
        n = len(nums)
        nums.sort()
        for i in range(n):
            if nums[i] > 0:
                break
            if i == 0 or nums[i] != nums[i-1]:
                lo = i+1
                hi = n-1
                while lo < hi:
                    tot = nums[i] + nums[lo] + nums[hi]
                    if tot == 0:
                        res.add(tuple([nums[i], nums[lo], nums[hi]]))
                        lo += 1
                        hi -= 1
                    elif tot < 0:
                        lo += 1
                    else:
                        hi -= 1
                    while nums[lo-1] == nums[lo] and lo < hi:
                        lo += 1
        return list(res)

            
            
        
                    

data = [-1,0,1,-2,2,3]

s = Solution()
res = s.threeSum(data)
print(res)