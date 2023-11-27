class test:
     
    def merge( nums1: list[int], m: int, nums2: list[int], n: int) -> None:
            """
            Do not return anything, modify nums1 in-place instead.
            """
            master_index = m + n - 1
            arr_1_index = m - 1
            arr_2_index = n - 1

            while master_index >= 0:
                if arr_1_index >= 0 and (arr_2_index < 0 or nums1[arr_1_index] > nums2[arr_2_index]):
                    nums1[master_index] = nums1[arr_1_index] 
                    arr_1_index -= 1
                else:
                    nums1[master_index] = nums2[arr_2_index] 
                    arr_2_index -= 1
                master_index -= 1


# test.merge(nums1 = [2,0], m = 1, nums2 = [1], n = 1)
# test.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)

    def removeElement(nums: list[int], val: int) -> int:
        curr_index = len(nums) - 1
        next_val_pos = curr_index
        count_of_num = 0

        if nums[curr_index] == val:
             count_of_num += 1
             curr_index -= 1
             next_val_pos -= 1

        while curr_index >= 0:
             if nums[curr_index] == val:
                  if curr_index < next_val_pos:
                       temp_num = nums[next_val_pos]
                       nums[next_val_pos] = nums[curr_index]
                       nums[curr_index] = temp_num
                       #next_val_pos = curr_index - 1
                  #else:
                  next_val_pos -= 1
                  count_of_num +=1                  
                  curr_index -= 1
             else:
                curr_index -= 1
        return count_of_num
             


# nums = [3,2,2,3]
# val = 3
nums = [0,1,2,2,3,0,4,2]
val = 2
k = test.removeElement(nums, val)