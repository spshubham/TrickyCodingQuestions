"""
Search Insert Position
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:
Input: [1,3,5,6], 5
Output: 2

Example 2:
Input: [1,3,5,6], 2
Output: 1

"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)
        # Input: [1,3,5,6], 2 # Output: 1
        while low < high:
            mid = low + (high - low) // 2 
            if nums[mid] >= target:
                high = mid
            else:
                low = mid + 1
        return low
            