class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        l = sorted(nums)
        x = []
        for i in range(len(l)):
            if l[i] > target:
                break;
            elif l[i] == target:
                x.append(i)
        return x
