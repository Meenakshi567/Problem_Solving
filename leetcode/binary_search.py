class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid = len(nums)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            for i in range(0,mid):
                if nums[i] == target:
                    return i
                    break
            return -1
        elif nums[mid] < target:
            for i in range(mid,len(nums)):
                if nums[i] == target:
                    return i
            return -1
