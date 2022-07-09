"""
Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0
"""

def lengthOfLongestSubstring(s: str) -> int:
    substring = ''
    longest_substring = ''
    for char in s:
        if not char in substring:
            substring += char
        else:
            if len(longest_substring) < len(substring):
                longest_substring = substring
            substring = substring[substring.index(char)+1:] + char
    return max(len(longest_substring), len(substring))

if __name__ == '__main__':
    print(lengthOfLongestSubstring('abcabcbb'))  # Result: 3
    print(lengthOfLongestSubstring('bbbbb'))  # Result: 1
    print(lengthOfLongestSubstring('pwwkew'))  # Result: 3
    print(lengthOfLongestSubstring(''))  # Result: 0
    print(lengthOfLongestSubstring(' '))  # Result: 1
    print(lengthOfLongestSubstring('dvdf'))  # Result: 1