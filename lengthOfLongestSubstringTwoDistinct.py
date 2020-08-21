"""
Longest Substring with At Most 
Two Distinct Characters
Given a string s , find the length 
of the longest substring t  that contains 
at most 2 distinct characters.

Example 1:
Input: "eceba"
Output: 3
Explanation: t is "ece" which its length is 3.

"""

class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        start, end, maxLenSoFar = 0, 0, 0
        letterByFrequency = {}
        
        while end < len(s):
            rightChar = s[end]
            if rightChar not in letterByFrequency:
                letterByFrequency[rightChar] = 0
            letterByFrequency[rightChar] += 1
            
            #Maintain the size of map to 2 distinct chars
            while len(letterByFrequency) > 2:
                leftChar = s[start]
                letterByFrequency[leftChar] -= 1

                # remove letter which is no longer fit in the window
                if letterByFrequency[leftChar] == 0:
                    del letterByFrequency[leftChar]
                # shift the window 
                start += 1
            # update max length
            maxLenSoFar = max(maxLenSoFar, end - start + 1)
            end += 1
        return maxLenSoFar