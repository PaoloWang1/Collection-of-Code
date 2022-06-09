def bubble_sort(nums):
    if len(nums) == 1:
        return nums
    for x in range(len(nums)-1):
        if nums[x] > nums[x+1]:
            nums[x], nums[x+1] = nums[x+1], nums[x]

    big = nums[-1]
    d = bubble_sort(nums[:-1])
    return d + [big]

print(bubble_sort([7,4,5,11,2,2,3]))
