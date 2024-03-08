class Solution:
    def twoSum(self, nums, target):
        for i, a in enumerate(nums):
            for j, b in enumerate(nums):
                if i != j and i < j and ( a + b ) == target:
                    return [i,j]

ts = Solution()

print(ts.twoSum([2,7,11,15], 9)) # [0,1]
print(ts.twoSum([3,2,4], 6)) # [1,2]
print(ts.twoSum([3,3], 6)) # [0,1]
print(ts.twoSum([0,4,3,0], 0)) # [0,3]