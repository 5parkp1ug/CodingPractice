"""
Given a string s and a string array dictionary, return the longest string in the dictionary 
that can be formed by deleting some of the given string characters. If there is more than one 
possible result, return the longest word with the smallest lexicographical order. 
If there is no possible result, return the empty string.

Example 1:
Input: s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]
Output: "apple"

Example 2:
Input: s = "abpcplea", dictionary = ["a","b","c"]
Output: "a"
"""
def generator(string: str):
	result = []

	for i in range(0, 1<<len(string)):
		temp_string=''
		for j in range(len(string)):
			if (i>>j) & 1 != 0:
				temp_string+=string[j]
		result.append(temp_string)
	return result
def find_longest_word(s: str, dictionary: list) -> str:
	string_list = generator(s)
	longest_str = ''
	for word in dictionary:
		if word in string_list:
			if len(word) > len(longest_str):
					longest_str = word
			elif len(word) == len(longest_str):
				if word < longest_str:
					longest_str = word  
	return longest_str

print(find_longest_word(s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]))
print(find_longest_word(s = "abpcplea", dictionary = ["abce","abca","c"]))