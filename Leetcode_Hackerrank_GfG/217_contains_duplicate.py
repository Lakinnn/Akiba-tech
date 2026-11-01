class  solution(object):
	def contain_duplicate(self, nums):
		nums.sort()
		for i in range(0, len(nums)-1):
			return True
		return False
