class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        count = 0
        presum = {0:1}
        running_sum = 0

        for i in range(len(nums)):
            running_sum+=nums[i]
            needed = running_sum-k
            if needed in presum:
                count+=presum[needed]
            presum[running_sum]=presum.get(running_sum,0)+1

        return count
