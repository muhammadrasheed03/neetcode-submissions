class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        sorted_nums = sorted(nums)

        if len(sorted_nums)==0:
            return 0
        
        current_streak = 1
        max_streak = 1

        for i in range(1, len(nums)):
            if sorted_nums[i]==sorted_nums[i-1]:
                current_streak +=0

            elif (sorted_nums[i]-sorted_nums[i-1]==1):
                current_streak+=1
            else:
                current_streak = 1

            max_streak = max(current_streak, max_streak)
        return max_streak
        