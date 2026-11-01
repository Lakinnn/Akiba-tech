class Solution:
	def missing_num(self, nums: List[int])-> int:
		n =len(nums)
		return (1+n)*n // 2 - sum(nums)