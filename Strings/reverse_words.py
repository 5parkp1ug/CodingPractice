def reverseWords(s: str) -> str:
	start = len(s) - 1
	end = start
	string = []
	while end > -1 or start > -1:
		while s[end] == ' ' and end > -1:
			end -= 1
		start = end
		while s[start] != ' ' and start > -1:
			start-=1

		string.append(s[start+1: end+1])
		end = start
		start -= 1
		end -= 1
	return ' '.join(string).rstrip()

print(reverseWords("the sky is blue"))
print(reverseWords("  hello world  "))
print(reverseWords("a good   example"))
print(reverseWords("Alice does not even like bob"))
print(reverseWords("  Bob    Loves  Alice   "))