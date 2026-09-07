class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict = collections.Counter(nums)
        mydict = dict(sorted(mydict.items(), key=lambda item:item[1], reverse=True))
        return [x for x in list(mydict.keys())[0:k]]