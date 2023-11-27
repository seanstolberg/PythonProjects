class Solution:
    def twoSum(nums: list[int], target: int) -> list[int]:
        num_indices = {}

        for i, num in enumerate(nums):

            complement = target - num

            if complement in num_indices:
                return [num_indices[complement], i]
            
            num_indices[num] = i

        return []


print(Solution.twoSum(nums = [2,7,11,15], target = 9)) # [0,1]
print(Solution.twoSum(nums = [3,2,4], target = 6)) # [1,2]
print(Solution.twoSum(nums = [3,3], target = 6)) # [0,1]