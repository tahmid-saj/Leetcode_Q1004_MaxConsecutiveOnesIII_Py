class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxLength, windowStart, numZeroes = 0, 0, 0

        for windowEnd in range(0, len(nums)):
            if nums[windowEnd] == 0: numZeroes += 1

            while numZeroes > k:
                if nums[windowStart] == 0: numZeroes -= 1
                windowStart += 1
            
            maxLength = max(maxLength, windowEnd - windowStart + 1)

        return maxLength
