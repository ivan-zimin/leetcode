from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        product = 1
        for num in nums:
            ans.append(product)
            product *= num
        product = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= product
            product *= nums[i]
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.productExceptSelf([1, 2, 3, 4]))


# bruteforce solution
"""
from functools import reduce

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = []
        for i, val in enumerate(nums):
            tmp = nums[:i] + nums[i+1:]
            arr.append(reduce(lambda x, y: x*y, tmp))
        return arr
"""