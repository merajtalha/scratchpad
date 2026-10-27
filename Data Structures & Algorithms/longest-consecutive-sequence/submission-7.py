class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        #print(nums)
        count = 1
        list2 = []
        length = len(nums)
        if length <= 0:
            return 0
        list2.append(count)
        for x in range(length - 1):
            if nums[x+1] == nums[x]:
                continue
            elif nums[x+1] - nums[x] == 1:
                count+=1
            else:
                count=1
            list2.append(count)
            #print(list2)
        return max(list2) if list2 else 0
            
        