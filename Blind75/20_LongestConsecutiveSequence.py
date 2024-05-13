class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        longest = 0

        for i in nums: 
            if(i - 1 not in setNums):
                length = 0
                while i + length in setNums:
                    length += 1
                longest = max(length , longest)

        return longest
