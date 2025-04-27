class Solution:
    result = 0

    def __init__(self, func, *args, **kwargs):
        if hasattr(self, func):
            print(f"Output of: {func}", getattr(self, func)(*args, **kwargs))
        else:
            print(f"Function: {func} not found")

    def singleNumber(self, nums):
        self.result = 0
        for num in nums:
            self.result ^= num
        return self.result

    def XorOperation(self, n, start):
        nums = [start + (2 * i) for i in range(n)]

        self.result = nums[0]

        for num in nums[1:]:
            self.result ^= num
        return self.result

    def subsetXORSum(self, nums):
        self.result = 0
        size = len(nums)
        for i in range(size):
            num = 0
            for j in range(i, size):
                num = num ^ nums[j]
                self.result = self.result + num
        return self.result


Solution("singleNumber", [4, 3, 5, 4, 5])
Solution("XorOperation", 4, 3)
Solution("subsetXORSum", [5, 1, 6])


