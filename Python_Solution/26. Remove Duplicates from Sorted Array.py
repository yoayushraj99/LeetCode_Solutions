# Easy

def removeDuplicates(self, nums: List[int]) -> int:
    count = 0
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            count += 1
        else:
            nums[i + 1 - count] = nums[i + 1]
    return len(nums) - count
