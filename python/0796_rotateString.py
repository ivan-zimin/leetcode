class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            if s[i:] + s[0:i] == goal:
                return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.rotateString('abcde', 'bcdea'))