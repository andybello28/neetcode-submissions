class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for s in strs:
            ret += str(len(s)) + "#" + s
        return ret
        

    def decode(self, s: str) -> List[str]:
        ret = []
        print(s)
        #Current marks the start of the length of a certain string which could be more than
        current = 0
        while current < len(s):
            length = ""
            length_counter = current
            while s[length_counter] != "#":
                length += s[length_counter]
                length_counter += 1
            length = int(length)
            ret.append(s[length_counter + 1 : length_counter + length + 1])
            current = length_counter + length + 1
        return ret