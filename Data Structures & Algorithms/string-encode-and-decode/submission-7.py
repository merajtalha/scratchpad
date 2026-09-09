class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = []
        for x in strs:
            enc.append(str(len(x)))
            enc.append("#")
            enc.append(x)
        return "".join(enc)

    def decode(self, s: str) -> List[str]:
        #"3#gel4#neet."
        dec = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            elemlen = int(s[i:j])
            dec.append(s[j+1:j+1+elemlen])
            i = j + 1 + elemlen
        return dec
            




        