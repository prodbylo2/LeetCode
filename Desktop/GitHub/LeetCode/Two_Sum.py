# LEETCODE 1
# EASY

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:
# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]
#
# Example 2:
# Input: nums = [3, 2, 4], target = 6
# Output: [1, 2]
#
# Example 3:
# Input: nums = [3, 3], target = 6
# Output: [0, 1]


def twosum(nums,target):
    cmap = dict()       # creating a hashmap to store the difference between the target as key and the index as the value
    for i in range(len(nums)):

        compliment = target - nums[i]
        num = nums[i]

        if num in cmap:
            return [cmap[num], i]


        else:
            cmap[compliment] = i

    return []

print(twosum([2,7,11,15],9))