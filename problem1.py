

## Problem 1

#https://leetcode.com/problems/product-of-array-except-self/

"""
Given an array nums of n integers where n > 1, 
return an array output such that output[i] is equal to the product of all the elements of nums 
except nums[i].

Example:

Input: [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? 
(The output array does not count as extra space for the purpose of space complexity analysis.)
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [0 for i  in range(n)]           #Initilize left product 
        right = [0 for i  in range(n)]          #initilize right product array
        prod = [0 for i  in range(n)]           #initilize the prod array
        
        left[0] = nums[0]                       #calculate the left prefix product
        for i in range(1, n):
            left[i] = left[i-1] * nums[i]
            
        right[n-1] = nums[n-1]                  #calculate the right prefix product
        for i in range(n-2, -1, -1):
            right[i] = right[i+1] * nums[i]
            
        for i in range(n):
            if i == 0:                          #edge case of first index
                prod[i] = right[i+1]
            elif i == n - 1:                    #edge case of late index
                prod[i] = left[i-1]
            else:
                prod[i] = left[i-1] * right[i+1]    #use solution from left and right array
                
        return prod