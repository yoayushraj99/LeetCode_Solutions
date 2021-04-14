# Easy

def removeElement(self, nums: List[int], val: int) -> int:
    length = len(nums)
    while val in nums: nums.remove(val)
    return length
