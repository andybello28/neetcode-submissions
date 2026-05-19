class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Something is the start of a sequence if the number before it is not in there
        s = set(nums)
        sequences = []

        for num in s:
            if num - 1 not in s:
                sequences.append([num])

        for sequence in sequences:
            start = sequence[0]
            while start + 1 in s:
                sequence.append(start + 1)
                start += 1

        max_length = 0
        for sequence in sequences: 
            if len(sequence) > max_length:
                max_length = len(sequence)
        return max_length