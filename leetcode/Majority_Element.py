from collections import Counter 
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = Counter(nums)
        (num,count) = freq.most_common(1)[0]
        return num
