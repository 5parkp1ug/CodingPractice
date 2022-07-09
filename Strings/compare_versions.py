def compareVersion(version1: str, version2: str) -> int:
	start1 = 0
	end1 = 0
	ver1 = ''
	start2 = 0
	end2 = 0
	ver2 = ''
	result = 0
	
	while end1 < len(version1) or end2 < len(version2):
		
		print(end1)
		while version1[end1] != '.' and end1 < len(version1):
			end1 += 1
		ver1 = version1[start1:end1]
		start1 = end1

		while version2[end2] != '.' and end2 < len(version2):
			end2 += 1
		ver2 = version2[start2:end2]
		start2 = end2 = end2 + 1

		print(f'ver1={ver1} ver2={ver2}')
		if ver1 != ver2:
			if int(ver1) < int(ver2): 
				result = -1
				break
			elif int(ver1) > int(ver2):
				result = 1

		end1 += 1
		end2 += 1

	return result

# print(compareVersion(version1 = "1.01", version2 = "1.001"))
print(compareVersion(version1 = "1.0", version2 = "1.0.0"))
# print(compareVersion(version1 = "7.5.2.4", version2 = "7.5.3"))
# print(compareVersion(version1 = "1.0.1", version2 = "1"))