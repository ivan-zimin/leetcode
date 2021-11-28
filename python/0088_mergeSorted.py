from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        m -= 1
        n -= 1
        index = len(nums1) - 1
        while index >= 0:
            if m < 0:
                nums1[index] = nums2[n]
                n -= 1
            elif n < 0:
                nums1[index] = nums1[m]
                m -= 1
            else:
                if nums1[m] > nums2[n]:
                    nums1[index] = nums1[m]
                    m -= 1
                else:
                    nums1[index] = nums2[n]
                    n -= 1
            index -= 1


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3

    s = Solution()
    s.merge(nums1, m, nums2, n)
    print(nums1)