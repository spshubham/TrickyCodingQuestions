"""
Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.

Example 1:
Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].
"""

def maxSubArray(nums, k):
  maxSoFar = 0 
  maxEndHere = 0
  start = 0
  end = 0;
  while end < len(nums)):
    maxEndHere += nums[end]
    # Maintain the size of window equal to k
    if end >= k-1:
      maxSoFar = max(maxSoFar, maxEndHere)
      maxEndHere -= nums[start]  # remove first element in the window
      start += 1 # shift the window

    end += 1
  return maxSoFar
