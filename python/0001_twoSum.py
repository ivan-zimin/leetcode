from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i_index, i_element in enumerate(nums):
            for j_index, j_element in enumerate(nums):
                if (i_element + j_element == target) and (i_index != j_index):
                    return [i_index, j_index]


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))
