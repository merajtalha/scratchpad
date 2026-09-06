class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        items = {}
        for i, n in enumerate(nums):
            items[n] = i
        
        for x in range(len(nums)):
            diff = target - nums[x]
            if diff in items and items[diff] != x:
                return [x, items[diff]]

        return []
        

