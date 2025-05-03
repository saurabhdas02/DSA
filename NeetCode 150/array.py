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

    def hasDuplicateOptimisedSorting(arr):
        nums = arr.sort()
        for i in range(1, len(arr)):
            if nums[i] == nums[i-1]:
                return True
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
            diff = target - arr[i]
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]
            indices[n] = i


def ThreeSum(nums):
    def TwoPointer(nums):
        res = []
        nums.sort()
        for i, num in enumerate(nums):
            if num > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                threesum = num + nums[l] + nums[r]
                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res


def GroupAnagram(strs):
    def BruteForce(strs):
        result = defaultdict(list)
        for s in strs:
            sorted_s = "".join(sorted(s))
            result[sorted_s].append(s)
        return list(result.values())

    def characterCount(strs):
        result = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            result[tuple(count)].append(word)
        return list(result.values())

    strs = ['eat', 'ate', 'tea', 'alb', 'bal']
    print(characterCount(strs))
    print(BruteForce(strs))


def KFrequentItems(data, k):
    def BruteForce(nums, k):
        count = {}
        for item in nums:
            count[item] = 1 + count.get(item, 0)

        print(count)
        arr = []
        for item, cnt in count.items():
            arr.append([cnt, item])
        arr.sort()

        print(arr)
        result = []
        while len(result) < k:
            val = arr.pop()
            result.append(val[1])

        return result

    def usingHeap(nums, k):
        from collections import Counter
        import heapq
        freq = Counter(nums)

        return [item for item, _ in heapq.nlargest(k, freq.items(), key=lambda x: x[1])]

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

    # print(BruteForce(data, k))
    print(UsingBucketSort(data, k))


def ProductExceptSelf(nums):
    n = len(nums)
    result = [1] * n
    prefix = 1
    suffix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]
    return result


def isValidSudoku(board):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    subgrids = [set() for _ in range(9)]

    for r in range(9):
        for c in range(9):
            num = board[r][c]
            if num == ".":
                continue
            subgrid_index = (r // 3) * 3 + (c // 3)
            if num in rows[r] or num in cols[c] or num in subgrids[subgrid_index]:
                return False

            rows[r].add(num)
            cols[c].add(num)
            subgrids[subgrid_index].add(num)
    return True


def longestConsecutive(nums):
    nums_set = set(nums)
    longest = 0
    for num in nums_set:
        if num - 1 not in nums_set:
            current = num
            streak = 1
            while current + 1 in nums_set:
                current += 1
                streak += 1

            longest = max(longest, streak)
    return longest


def isPalindrome(s):
    def BruteForce(s):
        cleaned = ''.join(c.lower() for c in s if c.isalnum())
        return cleaned == cleaned[::-1]

    def TwoPointer(s):
        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True


def MaxArea(height):
    l, r = 0, len(height) - 1
    res = 0
    while l < r:
        area = min(height[l], height[r]) * (r - l)
        res = max(res, area)
        if height[l] <= height[r]:
            l += 1
        elif height[r] < height[l]:
            r -= 1
    return res


def MaxProfit(prices):
    def maxProfitSlidingWindow(prices):
        l, r = 0, 1
        maxP = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                maxP = max(maxP, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return maxP

    def MaxProfitDP(prices):
        maxP = 0
        minBuy = prices[0]

        for sell in prices:
            maxP = max(maxP, sell - minBuy)
            minBuy = min(minBuy, sell)
        return maxP


def lengthOfLongestSubstring(s):
    def SlidingWindow(s):
        l, r = 0, 1
        my_string = s[l]
        maxL = len(my_string)
        while r < len(s):
            # print(my_string)
            if s[r] not in my_string:
                my_string += s[r]
                r += 1
                maxL = max(maxL, len(my_string))
            else:
                maxL = max(maxL, len(my_string))
                l += 1
                r = l
                my_string = ""
            print(my_string)
        return maxL

    def Sliding(s):
        mp = {}
        l = 0
        res = 0
        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]] +1, l)
            mp[s[r]] = r
            res = max(res, r - l + 1)
    print(SlidingWindow(s))


# arr = [1, 2, 2, 3, 3, 3, 4]
# k = 2
# KFrequentItems(arr, k)
lengthOfLongestSubstring("aab")










