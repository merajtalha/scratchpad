class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict = {}
        for x in strs:
            newx = "".join(sorted(x))
            if newx not in mydict:
                mydict[newx] = [x]
            else:
                mydict[newx].append(x)
        return list(mydict.values())