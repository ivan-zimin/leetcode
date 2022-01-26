# this solution can be better

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x_bin = str(format(x, '#0100b'))
        y_bin = str(format(y, '#0100b'))
        dist = 0
        for i in range(len(x_bin)):
            if x_bin[i] != y_bin[i]:
                dist += 1
        return dist


if __name__ == '__main__':
    s = Solution()
    print(s.hammingDistance(1, 3))