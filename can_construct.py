def can_construct(targetStr: str, arr: list, memo = None) -> bool:
	if memo == None: memo = {}

	if targetStr in memo: return memo[targetStr]

	if targetStr == '': return True

	for word in arr:
		if targetStr.startswith(word):  # if the target/remaiing string starts with the word from wordbank
			remaining_string = targetStr.removeprefix(word)  # for python < 3.9 use --> x[len(y):]
			if can_construct(remaining_string, arr, memo):
				memo[remaining_string] = True
				return True
	memo[targetStr] = False
	return False

if __name__ == '__main__':
	print(can_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))  # Result: True
	print(can_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))  # Result: False
	print(can_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))  # Result: True
	print(can_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', [
		'e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'
	])) # Result : False