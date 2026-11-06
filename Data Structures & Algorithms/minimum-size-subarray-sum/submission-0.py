class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        min_length = len(nums)+1

        left = 0
        window_sum = 0

        for right in range(len(nums)):
            window_sum += nums[right]

            while window_sum >=target:
                cur_length = right-left+1
                min_length = min(min_length, cur_length)
                window_sum -= nums[left]
                left +=1

        if min_length == len(nums)+1:
            return 0

        else:
            return min_length

        