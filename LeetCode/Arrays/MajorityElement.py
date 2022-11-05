# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than
#  ⌊n / 2⌋ times. You may assume that the majority element
#   always exists in the array.

# Beats 95% apparently
def majorityElement(nums):
		if nums==[]:
			return 0
		n=set(nums)
		maxm = 0
		for x in n:
			t = nums.count(x)
			if t>maxm:
				maxm=t
				m=x
		return m
print(majorityElement([6,5,5]))

# my Solution terible runtime beats 18%
# def majorityElement(nums):
#         nums.sort()
#         if(len(nums) == 1):
#             return nums[0]
#         if(len(nums) % 2 == 0):
#             return nums[(len(nums) // 2) - 1]
#         else:
#             return nums[(len(nums) // 2)]
# print(majorityElement([3,4,3]))

# Boyer Moore Majority Voting
# def majorityElement(nums):
#         candidate = nums[0]
#         vote = 0 
#         for i in nums:
#             if(i == candidate):
#                 vote += 1 
#             else:
#                 vote -= 1 
#             if(vote == 0):
#                 candidate = i 
#                 vote = 1 
#             if(vote > len(nums)//2):
#                 return candidate
#         return candidate
# print(majorityElement([6,5,5]))



