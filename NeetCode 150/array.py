from collections import defaultdict


def hasDuplicate(arr):
    """
    check for Duplicate value
    """
    def hasDuplicateBruteForce(arr):
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i] == arr[j]:
                    return True
        return False

    def hasDuplicateOptimised(arr):
        seen = set()
        for num in arr:
            if num in seen:
                return True
            seen.add(num)
        return False


def checkAnagram(str1, str2):
    if len(str1) != len(str2):
        return False

    dict1 = {}
    dict2 = {}
    for i in range(len(str1)):
        dict1[str1[i]] = 1 + dict1.get(str1[i], 0)
        dict2[str2[i]] = 1 + dict2.get(str2[i], 0)

    return dict1 == dict2


def TwoSum(arr, target):
    def TwoSumBruteForce(arr, target):
        size = len(arr)
        for i in range(size):
            for j in range(i + 1, size):
                if arr[i] + arr[j] == target:
                    return [i, j]

    def TwoSumBinarySearch(arr, target):
        size = len(arr)
        arr = arr.sort()
        for i in range(size):
            value = target - arr[i]
            low = i+1
            high = size - 1
            while low <= high:
                mid = (low + high)//2
                if arr[mid] == value:
                    return [i, mid]
                elif arr[mid] > value:
                    high = mid - 1
                elif arr[mid] < value:
                    low = mid + 1
        return -1

    def TwoSumHashMap(arr, target):
        indices = {}
        for i, n in enumerate(arr):
            indices[n] = i

        for i, n in enumerate(arr):
            diff = target - arr[i]
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]


def GroupAnagram(strs):
    def BruteForce(strs):
        result = defaultdict(list)
        for s in strs:
            sorted_s = "".join(sorted(s))
            result[sorted_s].append(s)
        return list(result.values())

    def hashTable(strs):
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())

    def characterCount(strs):
        result = defaultdict()

        for word in strs:
            count = [0] * 26
            for s in word:
                count[ord(s) - ord('a')] += 1

            result[tuple(count)].append(s)
        return list(result.values())

    strs = ['eat', 'ate', 'tea', 'alb', 'bal']
    print(characterCount(strs))
    print(hashTable(strs))


def KFrequentItems(nums, k):
    def BruteForce(nums, k):
        count = {}
        for item in nums:
            count[item] = 1 + count.get(item, 0)

        arr = []
        for item, cnt in count.items():
            arr.append([cnt, item])
        arr.sort()

        result = []
        while len(result) < k:
            val = arr.pop()
            result.append(val[1])

        return result

    def UsingBucketSort(nums, k):
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        print(count)

        for num, cnt in count.items():
            freq[cnt].append(num)

        result = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)
            if len(result) == k:
                return result

    print(BruteForce(arr, k))
    print(UsingBucketSort(arr, k))


arr = [1, 2, 2, 3, 3, 3, 4]
k = 2
KFrequentItems(arr, k)










