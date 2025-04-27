class Solution:
    result = 0

    def __init__(self, func, *args, **kwargs):
        if hasattr(self, func):
            print(f"Output of: {func}", getattr(self, func)(*args, **kwargs))
        else:
            print(f"Function: {func} not found")

    @classmethod
    def firstOccurrence(cls, array, target):
        low = 0
        high = len(array) - 1

        if array[low] == target:
            return low
        while low <= high:
            mid = (low + high) // 2
            print(f"low: {low}, mid: {mid}, high: {high}")

            if array[mid - 1] != target and array[mid] == target:
                return mid

            elif array[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    @classmethod
    def lastOccurrence(cls, array, target):
        low = 0
        high = len(array) - 1

        if array[high] == target:
            return high
        while low <= high:
            mid = (low + high) // 2
            print(f"low: {low}, mid: {mid}, high: {high}")

            if mid == len(array) - 1 or array[mid + 1] != array[mid]:
                return mid
            if array[mid] > target:
                high = mid - 1
            elif array[mid] < target:
                low = mid + 1
            else:
                low += 1
        return -1

    def countOccurrence(self, array, target):
        first_occurrence = self.firstOccurrence(array, target)
        if first_occurrence < 0:
            return 0
        return self.lastOccurrence(array, target) - first_occurrence + 1

    def countOccurrenceAlternate(self, array, target):
        first_occurrence = self.firstOccurrence(array, target)
        if first_occurrence < 0:
            return 0
        else:
            count = 1
            for i in range(first_occurrence + 1, len(array)):
                if array[i] == target:
                    count += 1
                else:
                    break
        return count

    @classmethod
    def sqrt(cls, x):
        low = 0
        high = x
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            print(f"low: {low}, mid: {mid}, high: {high}")
            msq = mid*mid

            if msq == x:  # msq <=x && (mid+1) * (mid +1) > x
                return mid
            elif msq > x:
                high = mid - 1
            else:
                low = mid + 1
                ans = mid
        return ans

    @classmethod
    def AlternateSqrt(cls, x):
        low = 1
        high = x
        while low <= high:
            mid = low + (high-low)//2
            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            if mid * mid > x:
                high = mid - 1
            else:
                low = mid + 1

    @classmethod
    def checkRotatedAndSorted(cls, array):
        """
        Check if array is sorted and rotated
        :return:
        """
        c = 0
        for i in range(len(array)):
            if array[i] > array[(i + 1) % len(array)]:
                c += 1
            if c > 1:
                return False
        return True

    @classmethod
    def minRotatedSorted(cls, array):
        low = 0
        high = len(array) - 1
        if array[low] < array[high]:
            return low
        while low <= high:
            mid = (low + high) // 2
            print(f"low: {low}, mid: {mid}, high: {high}")
            if array[mid - 1] > array[mid]:
                return mid
            elif array[mid] > array[high]:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    @classmethod
    def findSingleElement(cls, array):

        if len(array) == 1 or array[0] != array[1]:
            return array[0]
        if array[-1] != array[-2]:
            return array[-1]

        low = 2
        high = len(array) - 3

        while low <= high:
            mid = (low + high) // 2
            print(f"low: {low}, mid: {mid}, high: {high}")
            if array[mid] != array[mid - 1] and array[mid] != array[mid + 1]:
                return array[mid]
            if mid % 2 == 0:
                if array[mid] == array[mid + 1]:
                    low = mid + 2
                else:
                    high = mid - 2
            else:
                if array[mid] == array[mid + 1]:
                    high = mid - 1
                else:
                    low = mid + 1
        return -1

    @classmethod
    def findSingleElementAlternate(cls, array):
        if len(array) == 1 or array[0] != array[1]:
            return array[0]
        if array[-1] != array[-2]:
            return array[-1]

        low = 2
        high = len(array) - 3

        while low < high:
            mid = low + (high - low) // 2
            print(f"low: {low}, mid: {mid}, high: {high}")
            if mid % 2 == 1:
                mid -= 1
            if array[mid] == array[mid + 1]:
                low = mid + 2
            else:
                high = mid
        return array[low]

    @classmethod
    def arrayIntersection(cls, array1, array2, sort=True):
        if sort:
            array1.sort()
            array2.sort()
        i, j = 0, 0
        result = list()
        while i < len(array1) and j < len(array2):
            if array1[i] < array2[j]:
                i += 1
            elif array1[i] > array2[j]:
                j += 1
            else:
                result.append(array1[i])
                i += 1
                j += 1
        return result

    @classmethod
    def binarySearchNegative(cls, array):
        count = 0
        start = 0
        end = len(array) - 1
        while start <= end:
            print("Start: ", start, "End: ", end)
            mid = start + (end - start) // 2
            print("mid: ", mid, "array[mid]: ", array[mid])
            if array[mid] < 0:
                end = mid - 1
            else:
                start = mid + 1
        # print(end)
        count = abs(len(array) - end - 1)
        return count

    @classmethod
    def searchInRotatedSortedArray(cls, array, target):
        """
        https://getsdeready.com/courses/design-dsa-combined/lesson/search-in-rotated-sorted-array-2/
        :param array:
        :param target:
        :return:
        """
        low = 0
        high = len(array) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if array[mid] == target:
                return mid
            if array[low] <= array[mid]:
                if array[low] <= target < array[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if array[mid] < target <= array[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1

    @classmethod
    def findPeakElement(cls, array):
        low = 0
        high = len(array) - 1
        while low <= high:
            mid = low + (high - low) // 2
            print("Start: ", low, "End: ", high)
            print("mid: ", mid, "array[mid]: ", array[mid])
            if array[mid - 1] < array[mid] > array[mid + 1]:
                return array[mid]
            elif array[mid] < array[mid + 1]:
                low = mid + 1
            else:
                high = mid - 1

    @classmethod
    def findNegativeInArray(cls, array):
        """
        https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
        :param array:
        :return:
        """
        count_negative = 0
        for i in range(len(array)):
            print("i: ", i)
            start = 0
            end = len(array[i]) - 1
            while start <= end:
                print("Start: ", start, "End: ", end)
                mid = start + (end - start) // 2
                print(array[mid])
                if array[i][mid] < 0:
                    end = mid - 1
                else:
                    start = mid + 1
            # print(end)
            count_negative += len(array[i]) - start
            # count_negative += self.binarySearchNegative(array[i])
            print(f"Count Negative: {count_negative}")
        return count_negative

    @classmethod
    def swapsToSort(cls, nums):
        """
        https://getsdeready.com/courses/design-dsa-combined/lesson/minimum-swaps-to-sort-2/
        :param nums:
        :return:
        """
        temp = sorted(nums)
        hash_map = {temp[i]: i for i in range(len(nums))}
        ans = 0
        left = 0
        while left <= len(nums) - 1:
            if left == hash_map[nums[left]]:
                left += 1
            else:
                temp = nums[hash_map[nums[left]]]
                nums[hash_map[nums[left]]] = nums[left]
                nums[left] = temp
                ans += 1
        return ans

    @classmethod
    def binarySearchLessOrEqual(cls, row, target):
        low = 0
        high = len(row) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if row[mid] <= target:
                low = mid + 1
            else:
                high = mid - 1
        return low

    def countLessOrEqual(self, matrix, target):
        count = 0
        for row in matrix:
            count += self.binarySearchLessOrEqual(row, target)
        return count

    def findMedian(self, matrix):
        row_length = len(matrix)
        column_length = len(matrix[0])

        low = float('inf')
        high = float('-inf')
        print(low, high)
        for row in matrix:
            low = min(low, row[0])
            high = max(high, row[-1])

        print(low, high)

        while low <= high:
            mid = low + (high - low) // 2
            count = self.countLessOrEqual(matrix, mid)
            if count <= (row_length * column_length) // 2:
                low = mid + 1
            else:
                high = mid - 1
        return low

    @classmethod
    def minimumSizeSubArraySum(cls, nums, target):
        """
        https://getsdeready.com/courses/design-dsa-combined/lesson/minimum-size-subarray-sum-3/
        :param nums:
        :param target:
        :return:
        """
        a = 0
        min_len = float('inf')
        curr_sum = 0
        for b in range(len(nums)):
            curr_sum += nums[b]
            if curr_sum >= target:
                curr_sum -= nums[a]
                min_len = min(min_len, b-a+1)
                a += 1
        return min_len if min_len != float('inf') else 0

    @classmethod
    def maxStairHeight(cls, N):
        import math
        x = math.sqrt(1 + 8 * N)

        height = int((int(x) - 1) / 2)

        return height

    @classmethod
    def maxStairHeightBinarySearch(cls, N):
        low = 0
        high = N
        ans = 0
        while low <= high:
            mid = low + (high - low)//2
            sum_blocks = (mid * (mid + 1)) // 2

            if sum_blocks <= N:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans

    @classmethod
    def arrayMergeSort(cls, array1, array2, sort=True):
        if sort:
            array1.sort()
            array2.sort()
        i, j = 0, 0
        result = list()
        while i < len(array1) and j < len(array2):
            # print("i: ", i, "j: ", j)
            # print(array1[i], array2[j])
            if array1[i] <= array2[j]:
                result.append(array1[i])
                i += 1
            elif array1[i] > array2[j]:
                result.append(array2[j])
                j += 1

        result.extend(array1[i:])
        result.extend(array2[j:])
        return result

    def medianOfTwoArray(self, array1, array2):
        final_sorted_array = self.arrayMergeSort(array1, array2, sort=False)
        print(final_sorted_array)
        median = 0
        if len(final_sorted_array) % 2 == 0:
            median = (final_sorted_array[len(final_sorted_array)//2] + final_sorted_array[(len(final_sorted_array)//2)+1])//2
        else:
            median = final_sorted_array[len(final_sorted_array) // 2]
        return median

    @classmethod
    def missingNumbers(cls, arr, brr):
        arr.sort()
        brr.sort()
        i, j = 0, 0
        missing_numbers = []
        while j < len(brr):
            if i < len(arr) and arr[i] == brr[j]:
                i += 1
                j += 1
            elif i < len(arr) and arr[i] < brr[j]:
                i += 1
            else:
                if not missing_numbers or missing_numbers[-1] != brr[j]:
                    missing_numbers.append(brr[j])
                j += 1

        return missing_numbers

    @classmethod
    def missingNumbersWithHash(cls, arr, brr):
        freq1 = {}
        freq2 = {}
        missing_numbers = []
        for num in arr:
            freq1[num] = freq1.get(num, 0) + 1

        for num in brr:
            freq2[num] = freq2.get(num, 0) + 1

        print(freq1, freq2)

        for num in freq2:
            print(num)
            if freq2[num] > freq1[num].get(num, 0):
                missing_numbers.append(num)

        return sorted(missing_numbers)

    @classmethod
    def find_equilibrium_index(cls, arr):
        total_sum = sum(arr)
        left_sum = 0
        for index, num in enumerate(arr):
            print("Total: ", total_sum, "LeftSum: ", left_sum)
            if left_sum == total_sum - left_sum - num:
                return index
            left_sum += num
        return -1

    @classmethod
    def reachANumberMinMoves(cls, target):
        start, end = 0, target

        while start <= end:
            mid = start + (end - start) // 2
            mid_sum = mid * (mid + 1) // 2
            print("mid: ", mid, "mid_sum: ", mid_sum)
            if mid_sum >= target and (mid_sum - target) % 2 == 0:
                end = mid
            else:
                start = mid + 1
        return start


search_array = [3, 3, 3, 4, 4, 5, 7, 8]
search_target = 3
rotated_search_array = [7, 8, 9, 1, 3, 4, 5]
single_array = [3, 3, 4, 4, 5, 5, 7, 8, 8, 9, 9]
peaked_array = [2, 1, 2, 4, 3, 4, 7, 8, 6]
swap_array = [4, 2, 3, 6]
median_array = [[1, 2, 3], [2, 3, 4], [1, 2, 3], [2, 3, 4]]
arr1 = [7, 2, 5, 3, 5, 3]
arr2 = [7, 2, 5, 4, 6, 3, 5, 3, 3]

# Solution("firstOccurrence", search_array, search_target)
Solution("lastOccurrence", search_array, search_target)
# Solution("countOccurrence", search_array, search_target)
# Solution("countOccurrenceAlternate", search_array, search_target)
# Solution("sqrt", 30)
# Solution("minRotatedSorted", rotated_search_array)
# Solution("findSingleElement", single_array)
# Solution("findSingleElementAlternate", single_array)
# Solution("arrayIntersection", [2, 4, 3, 54, 5, 4], [1, 4, 3, 5, 5, 4])
# Solution("binarySearchNegative", [54, 4, 2, -3,  -4, -54])
# negative_array_1 = [[5, -4], [4, -1]]
# negative_array = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3], [1, 1, -1, -2]]
# Solution("findNegativeInArray", negative_array_1)
# Solution("findNegativeInArray", negative_array)

# Solution("findPeakElement", peaked_array)
# Solution("swapsToSort", swap_array)
# Solution("findMedian", median_array)
# Solution("searchInRotatedSortedArray", rotated_search_array, 10)
# Solution("minimumSizeSubArraySum", [4, 5, 6, 7, 0, 1, 2, 3], 12)
# Solution("maxStairHeight", 28)
# Solution("maxStairHeightBinarySearch", 27)
# Solution("arrayMergeSort", [2, 3, 3, 4, 5, 5, 6], [1, 2, 4, 5, 5, 8], False)
# Solution("medianOfTwoArray", [2, 3, 3, 5, 5, 6], [1, 2, 4, 5, 5, 8])
# Solution("missingNumbers", arr1, arr2)
# Solution("missingNumbersWithHash", arr1, arr2)
# Solution("find_equilibrium_index", [2, 5, 6, 7])
# Solution("reachANumberMinMoves", 4)

