# Level :- Easy

def searchInsert(nums: List[int], target: int) -> int:
    start = 0
    end = len(nums) - 1

    if target > nums[-1]:
        return len(nums)

    if target < nums[0]:
        return 0

    while start <= end:
        mid = (start + end) // 2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            if mid - 1 >= 0:
                if target > nums[mid - 1]:
                    return mid
            end = mid - 1
        elif target > nums[mid]:
            if mid + 1 <= len(nums) - 1:
                if target < nums[mid + 1]:
                    return mid + 1
            start = mid + 1

    return -1
