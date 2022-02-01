# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

class Solution:
    def twoSum(self, nums: list[int], target: int):
        for i in range(0,len(nums)-1):
            for j in range((i+1),len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]

t = Solution()
print(t.twoSum([1,2,3,4,5,6],11))

#this above method consumes a lot of time to complete due to loops, 
#Alternative solution is


class Alternate:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(0,len(nums)-1):
            j = target - nums[i]
            if j in nums[i+1::]:
                return [i, nums[i+1::].index(j)+i+1]

T = Alternate()
print(T.twoSum([1,2,3,4,5,6],10))


#We can also solve this as below,
class AlgoSolution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        MyMap = dict()
        for i in range(len(nums)):
            if nums[i] in MyMap:
                return [MyMap[nums[i]],i]
            else:
                MyMap[target-nums[i]] = i

# The way this will work is that, given an input as [2,7,11,15], 18
# the interation will start with i = 0 and nums[i] = 2
# we will calculate the balance as 18 - 2 = 16
# we will see if 2 is in MyMap if not we will add a dictionary entry as "16":0 where we are saying 16 is in position 0
# now we go to the next iteration, where we are checking for 7
# balance will be 11, but this too is not in the mymap and we will add a new entry as "11": 1
# now when we iterate for 11 we get 7 as balance, and i value is now 2
# now we check if this 11 is in mymap and we have a entry as "11":1
# so we return the value of the "11" which is 1, and the i which is 2 

D = AlgoSolution()
print(D.twoSum([2,21,7,11,15],18))

    
