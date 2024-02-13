class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def check(arr, guess, k):
            total = 0
            count = 1
            for i in arr:
                if total + i > guess:
                    total = 0
                    count += 1
                total += i
            return count > k
                

        left = max(nums)
        right = sum(nums)

        while left<right:
            mid = (left+right)//2
            if check(nums, mid, k):
                left = mid + 1
            else:
                right = mid

        return left
