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

def find_longest_word(s: str, dictionary: list) -> str:
	longest_word = ''
	word_dict = {word:word for word in dictionary}
	for char in s:
		for index, word in enumerate(dictionary):
			if word_dict[word]!= '' and word_dict[word][0] == char:
				if len(word_dict[word][1:]) == 0:
					if len(word) > len(longest_word):
						longest_word = word
					elif len(word) == len(longest_word):
						if word < longest_word:
							longest_word = word
				else:
					word_dict[word] = word_dict[word][1:]
	return longest_word

print(find_longest_word(s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]))
print(find_longest_word(s = "abpcplea", dictionary = ["abce","abca","c"]))