class Solution:

    def removeDuplicates(nums: list[int]) -> int:
        # unique_set = set(nums)
        # matching_set = set()
        curr_pos = 0

        current_num = nums[curr_pos]
        # matching_set.add(current_num)
        curr_pos +=1
        next_swap_pos = curr_pos
        num_occurrences = 1
        while(curr_pos < len(nums)): #len(unique_set.difference(matching_set)) != 0 or 
            # if nums[curr_pos] == current_num:                
            while curr_pos < len(nums) and nums[curr_pos] == current_num:                
                if num_occurrences < 2:
                    next_swap_pos += 1 
                num_occurrences += 1 
                if curr_pos + 1 < len(nums):
                    curr_pos += 1
            current_num = nums[curr_pos]
            nums[next_swap_pos] = nums[curr_pos]
            # matching_set.add(current_num)
            next_swap_pos += 1
            num_occurrences = 1
            curr_pos += 1
            # current_num = nums[curr_pos]

        print(nums)
        return next_swap_pos





# print(Solution.removeDuplicates([1,1,1,2,2,3]))
print(Solution.removeDuplicates([0,0,1,1,1,1,2,3,3]))
