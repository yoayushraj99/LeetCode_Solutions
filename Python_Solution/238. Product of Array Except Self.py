from typing import *

def productExceptSelf(nums: List[int]) -> List[int]:
    n = len(nums)
    output = []
    
    prefix = 1
    for num in nums:
        output.append(prefix)
        prefix = prefix*num
        
    postfix = 1
    for i in range(n-1, -1, -1):
        output[i] = output[i]*postfix
        postfix = postfix*nums[i]
    return output