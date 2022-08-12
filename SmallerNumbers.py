class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = [0 for x in nums]
        for x in range(len(nums)):
            for y in nums:
                if y < nums[x]:
                    count[x] += 1
                    
        return count
