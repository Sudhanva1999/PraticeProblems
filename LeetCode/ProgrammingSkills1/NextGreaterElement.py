# The next greater element of some element x in an array is the first 
# greater element that is to the right of x in the same array.
# You are given two distinct 0-indexed integer arrays nums1 and nums2, 
# where nums1 is a subset of nums2.For each 0 <= i < nums1.length, 
# find the index j such that nums1[i] == nums2[j] and determine the 
# next greater element of nums2[j] in nums2. If there is no next
#  greater element, then the answer for this query is -1.
# Return an array ans of length nums1.length such that ans[i] is the
#  next greater element as described above.

# NON OPTMISED SOLUTION
def nextGreaterElement(nums1, nums2):
        solArr = []
        for i,numi in enumerate(nums1):
            equalIndex = -1
            flag = 0
            for j,numj in enumerate(nums2):
                if(numi == numj):
                    equalIndex = j
                if(j > equalIndex and flag == 0 and numj > numi and equalIndex != -1):
                    flag = 1
                    solArr.append(numj)
            if(flag == 0):
                solArr.append(-1)
        return solArr
print(nextGreaterElement([4,1,2],[1,3,4,2]))

# OPTIMISED SOLUTION
# def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
# 	if not nums2:
# 		return None

# 	mapping = {}
# 	result = []
# 	stack = []
# 	stack.append(nums2[0])

# 	for i in range(1, len(nums2)):
# 		while stack and nums2[i] > stack[-1]:       
# if stack is not empty, then compare it's last element with nums2[i]
# 			mapping[stack[-1]] = nums2[i]           
# if the new element is greater than stack's top element, then add this to dictionary 
# 			stack.pop()                             
# since we found a pair for the top element, remove it.
# 		stack.append(nums2[i])                      
# add the element nums2[i] to the stack because we need to find a number greater than this

# 	for element in stack:                           
# if there are elements in the stack for which we didn't find a greater number, map them to -1
# 		mapping[element] = -1

# 	for i in range(len(nums1)):
# 		result.append(mapping[nums1[i]])
# 	return result