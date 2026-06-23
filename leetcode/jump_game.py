class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        i = 0
        t= len(nums)-1
        while i< len(nums):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i+nums[i])
            if max_reach >=t:
                return True
            i += 1
        return max_reach >= t
