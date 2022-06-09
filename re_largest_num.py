def largest_num(nums):
    if len(nums) == 2:
        return(max(nums[0], nums[1]))
    num1 = nums[0]
    num3 = largest_num(nums[1:])
    return max(num1, num3)

print(largest_num([1000,2,3,555]))
