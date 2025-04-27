def SumOf3IntegerSameAsTarget(arr, target):
    arr.sort()
    print(arr)
    n = len(arr)
    for i in range(n - 2):
        left = i + 1
        right = n - 1
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            if current_sum == target:
                return True
            elif current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
    return False


# SumOf3IntegerSameAsTarget([1, 3, 4, 5, 6, 5, 5], 15)

