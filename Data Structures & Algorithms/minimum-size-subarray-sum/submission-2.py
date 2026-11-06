class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        left = 0
        window_sum = 0
        best = len(nums)+1

        for right, value in enumerate(nums):
            window_sum+=value

            while window_sum >= target:
                best = min(right-left+1, best)
                window_sum-=nums[left]
                left+=1
        return 0 if best == len(nums)+1 else best
        