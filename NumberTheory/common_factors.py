import sys


class Solution:

	def __init__(self, func, *args, **kwargs):
		if hasattr(self, func):
			print(getattr(self, func)(*args, **kwargs))
		else:
			print(f"Function: {func} not found")

	@classmethod
	def commonFactorsNaive(cls, a, b):
		count = 0
		for i in range(1, min(a, b) + 1):
			if a % i == 0 and b % i == 0:
				count += 1
		return count

	@classmethod
	def highest_gcd(cls, a, b):
		while b != 0:
			temp = b
			print(f"a:{a}, b:{b}, a%b: {a%b}")
			b = a % b
			a = temp
		return a

	@classmethod
	def count_divisors(cls, n):
		count = 0
		for i in range(1, int(n/2)):
			if n % i == 0:
				if n // i == i:
					count += 1
				else:
					count += 2
		return count

	def commonFactorsOptimal(self, a, b):
		gcd_val = self.highest_gcd(a, b)
		print("gcd_val", gcd_val)
		count = self.count_divisors(gcd_val)
		return count

	@classmethod
	def maths(cls, a, b):
		print(f"a/b: {a/b}, a//b: {a//b}, a%b: {a%b} ")

	@classmethod
	def factor_product(cls, n):
		product = 1
		for i in range(1, int(n/2)):
			if n % i == 0:
				if n//i == i:
					product = product*i
				else:
					product = product*i*(n//i)
		return product

	def gcd(self, a, b):
		if b == 0:
			return a
		return self.gcd(b, a % b)
	
	def repeatedGcd(self, N, x, y):
		print(N, x, y)
		g = self.gcd(x, y)
		return int(str(N)*g)


# Solution("repeatedGc", 123, 1,2)
# print(plus_one([9,9,9]))
# print(reverse_number(2984))
# print(commonFactorsOptimal(14,28))
# print(sol.highest_gcd(123123,123))
# print(commonFactorsNaive(14,28))
# maths(84, 15)
# print(count_divisors(number))

number = 17
Solution("factor_product", number)
Solution("gcd", 123123, 123123123)
Solution("repeatedGcd", 123, 2, 3)








