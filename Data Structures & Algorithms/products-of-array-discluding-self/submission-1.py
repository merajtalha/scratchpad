class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        product = 1
        for x in nums:
            res.append(product)
            product *= x
        product = 1
        for i in range(len(nums) -1, -1 , -1):
            res[i] *= product
            product *= nums[i]
        return res




        