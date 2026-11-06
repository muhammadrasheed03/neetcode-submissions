class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        count = 0
        running_sum = 0
        frequencies = {0:1}

        for num in nums:
            running_sum +=num
            count+= frequencies.get(running_sum-k, 0)
            frequencies[running_sum]=frequencies.get(running_sum,0)+1
        return count
        