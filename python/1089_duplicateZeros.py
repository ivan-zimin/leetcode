from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        l = len(arr)
        zeroes = arr.count(0)
        for i in range(l-1, -1, -1):
            if i + zeroes < l: # if the new position of the number is inside the array?
                arr[i + zeroes] = arr[i] # elements in original list are shifted to right by the number of 'zeroes'
            if arr[i] == 0: # if there is a Θ that should be included
                zeroes -= 1
                if i + zeroes < l:
                    arr[i + zeroes] = 0


if __name__ == '__main__':
    s = Solution()
    arr = [9,0,0,1,6,5,4,4]
    s.duplicateZeros(arr)
    print(arr)