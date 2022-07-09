"""
Longest Palindromic Substring
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Example 3:
Input: s = "a"
Output: "a"

Example 4:
Input: s = "ac"
Output: "a"
"""

def longest_palindrome(s: str) -> str:
    length = len(s)
    max_length = 1
    start = 0

    for index in range(1, length):
        # odd palindrome
        left = index - 1
        right = index + 1

        while(left >=0 and right < length and s[left]==s[right]):
            left -= 1
            right+= 1
        
        left += 1
        right -= 1

        if right - left + 1 > max_length:
            max_length = right - left + 1
            start = left

        # even palindrome
        left = index - 1
        right = index

        while(left >=0 and right < length and s[left]==s[right]):
            left -= 1
            right+= 1
        
        left += 1
        right -= 1

        if right - left + 1 > max_length:
            max_length = right - left + 1
            start = left
            
    return s[start:start+max_length]

if __name__ == '__main__':
    print(longest_palindrome('babad'))
    print(longest_palindrome('cbbd'))
    print(longest_palindrome('a'))
    print(longest_palindrome('ac'))