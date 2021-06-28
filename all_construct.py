def all_construct(targetStr: str, arr: list, memo = None) -> bool:
	if memo == None: memo = {}

	if targetStr in memo: return memo[targetStr]

	if targetStr == '': return [[]]

	results = []

	for word in arr:
		if targetStr.startswith(word):  # if the target/remaiing string starts with the word from wordbank
			suffix = targetStr.removeprefix(word)  # for python < 3.9 use --> x[len(y):]
			suffix_ways =  all_construct(suffix, arr, memo)
			target_ways = list(map(lambda way: [word] + way, suffix_ways))
			results.extend(target_ways)
	
	memo[targetStr] = results
	return results

if __name__ == '__main__':
	print(all_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))  # Result: 2
	print(all_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))  # Result: 1
	print(all_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))  # Result: 0
	print(all_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))  # Result: 4
	print(all_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeez', [
		'e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'
	])) # Result : 0