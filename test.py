class Solution:
    def twoSum(self, nums: list[int], target: int):
        for i in range(0,len(nums)-1):
            for j in range((i+1),len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]

t = Solution()
print(t.twoSum([1,2,3,4,5,6],11))