class Solution:

	def reverse_number(self, n):
		rev=0
		while n!=0:
			rem = n%10
			rev = rev*10 + rem
			n=n//10
		return rev


	def plus_one(self, n=[]):
		for i in range(len(n)-1,-1,-1):
			print(i, n[i])
			if n[i] != 9:
				n[i] += 1
				return n
			else:
				n[i]=0
		if n[0] == 0:
			return [1] + n

	def mySqrt(self, n):
		start=1
		end=n
		result=0

		while start <= end:
			print(start, end)
			mid = start + (end - start)//2
			if mid * mid == n:
				result = mid
				return result
			elif mid*mid > n:
				end = mid - 1
			else:
				result = mid
				start = mid + 1
		return result




solution = Solution()

# response = solution.plus_one([9,9,9])

response = solution.mySqrt(500)
print(response)
