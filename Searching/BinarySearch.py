class Solution:
    result = 0

    def __init__(self, func, *args, **kwargs):
        if hasattr(self, func):
            print(f"Output of: {func}", getattr(self, func)(*args, **kwargs))
        else:
            print(f"Function: {func} not found")

    @classmethod
    def linearSearch(cls, array, target):
        for i in range(len(array)):
            print(f"i: {i}, value: {array[i]}")
            if array[i] == target:
                return i
            i += 1
        return -1

    @classmethod
    def simpleBinarySearch(cls, array, target):
        low = 0
        high = len(array) - 1
        while low <= high:
            mid = (low + high) // 2
            print(f"low: {low}, mid: {mid}, high: {high}")
            if array[mid] == target:
                return mid
            elif array[mid] >= target:
                high = mid - 1
            else:
                low = mid + 1
        return -1

    def recursiveBinarySearch(self, array, target, low, high):
        if low > high:
            return -1
        mid = (low + high) // 2
        print(f"low: {low}, mid: {mid}, high: {high}")
        if array[mid] == target:
            return mid
        elif array[mid] >= target:
            high = mid - 1
            return self.recursiveBinarySearch(array, target, low, high)
        else:
            low = mid + 1
            return self.recursiveBinarySearch(array, target, low, high)

    def recursiveMain(self, array, target):
        return self.recursiveBinarySearch(array, target, 0, len(array) - 1)


search_array = [3, 3, 4, 4, 5, 7, 8]
search_target = 3
Solution("simpleBinarySearch", search_array, search_target)
# Solution("linearSearch", search_array, search_target)
Solution("recursiveMain", search_array, search_target)


