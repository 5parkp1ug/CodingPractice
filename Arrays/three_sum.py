"""Three Sum problem
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:
Input: nums = []
Output: []

Example 3:
Input: nums = [0]
Output: []
"""

def two_sum(targetSum: int, arr: list) -> list[list]:

    i = 0
    j = len(arr) - 1
    two_sums = []
    while i<j:
        if arr[i] + arr[j] > targetSum:
            j -= 1
        elif arr[i] + arr[j] < targetSum:
            i += 1
        elif arr[i] + arr[j] == targetSum:
            two_sums.append([arr[i], arr[j]])
            i += 1
            j -= 1
    return two_sums

def three_sum(nums: list) -> list[list]:

    nums = sorted(nums)
    three_sum_lists = []

    if len(nums) < 3:
        return []
    
    for index, num in enumerate(nums):
        result = two_sum(0-num, nums[index+1:])
        if result != []:
            for item in result:
                temp = [num, *item]
                if temp not in three_sum_lists:
                    three_sum_lists.append(temp)
    
    return three_sum_lists
	
if __name__ == '__main__':
    # print(three_sum([-1,0,1,2,-1,-4]))
    # print(three_sum([0,0,0,0]))
    print(three_sum([-2,0,1,1,2]))