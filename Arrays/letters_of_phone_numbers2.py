"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]
"""

def letter_combination(digits: str, memo={}) -> list[str]:
    table = ["0", "1", "abc", "def", "ghi", "jkl",
             "mno", "pqrs", "tuv", "wxyz"]

    combinations = []

    if digits == '':
        return []

    char_list = list(table[int(digits[0])])
    if digits[1:] in memo:
        result = memo[digits[1:]]
    else:
        result = letter_combination(digits[1:], memo)
        memo[digits] = result

    if result == []:
        result = ['']
    for char in char_list:
        for s in result:
            combinations.append(char + s)
    return combinations

if __name__ == '__main__':
    print(letter_combination("23"))
    # print(letter_combination(""))
    # print(letter_combination("2"))