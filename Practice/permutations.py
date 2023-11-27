class Solution:
    def permute(nums: list[int]) -> list[list[int]]:
        result = []

        # base case
        if (len(nums) == 1):
            return [nums[:]]

        for i in range(len(nums)):
            n = nums.pop(0)
            perms = Solution.permute(nums)

            for perm in perms:
                perm.append(n)
            result.extend(perms)
            # add back element 0 above
            nums.append(n)

        return result
    
# Example 1:

#Input: nums = [1,2,3]
#Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
print(Solution.permute(nums = [1,2,3]))

#Example 2:
#Input: nums = [0,1]
#Output: [[0,1],[1,0]]
print(Solution.permute(nums = [0,1]))

#Example 3:
#Input: nums = [1]
#Output: [[1]]
print(Solution.permute(nums = [1]))