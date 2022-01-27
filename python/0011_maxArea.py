from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        current_area = 0
        start = 0
        end = len(height) - 1

        while start < end:
            if height[start] <= height[end]:
                current_area = height[start] * (end - start)
                start += 1
            else:
                current_area = height[end] * (end - start)
                end -= 1
            if current_area > max_area:
                max_area = current_area

        return max_area


if __name__ == '__main__':
    s = Solution()
    print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))