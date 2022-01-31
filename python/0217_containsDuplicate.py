class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {i:0 for i in nums}
        for i in nums:
            d[i] += 1
        if sorted(d.values())[-1] == 1:
            return False
        return True