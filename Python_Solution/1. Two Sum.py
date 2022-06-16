# Easy

# Method-1 Naive Approach

def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

# Method-2 Pro Approach

def twoSum(self, nums: List[int], target: int) -> List[int]:
    dict = {}

    for index, item in enumerate(nums):
        diff = target - item
        if diff in dict:
            return [dict[diff], index]
        dict[item] = index
    return

