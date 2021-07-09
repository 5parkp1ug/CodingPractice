#!/usr/bin/env python3
# ==============================================================================
# Created By   : 5parkp1ug
# Description  : Count number of ways a given word can be generated using 
#                another given list of words
# ============================================================================

def count_construct(targetStr: str, arr: list, memo = None) -> bool:
	if memo == None: memo = {}

	if targetStr in memo: return memo[targetStr]

	if targetStr == '': return 1

	total_count = 0

	for word in arr:
		if targetStr.startswith(word):  # if the target/remaiing string starts with the word from wordbank
			remaining_string = targetStr.removeprefix(word)  # for python < 3.9 use --> x[len(y):]
			number_of_ways =  count_construct(remaining_string, arr, memo)
			total_count += number_of_ways
	
	memo[targetStr] = total_count
	return total_count

if __name__ == '__main__':
	print(count_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))  # Result: 2
	print(count_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))  # Result: 1
	print(count_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))  # Result: 0
	print(count_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))  # Result: 4
	print(count_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', [
		'e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'
	])) # Result : 0