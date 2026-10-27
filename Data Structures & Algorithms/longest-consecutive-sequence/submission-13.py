class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        count = 1
        max_val = 1
        length = len(nums)
        if length <= 0:
            return 0
        for x in range(length - 1):
            a = nums[x+1] - nums[x]
            if not a:
                continue
            if a == 1:
                count+=1
                if max_val >= count:
                    continue
                else:
                    max_val = count
            else:
                count=1
        return max_val

            
        