from .LinkedList.main import Node


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


def missingNumberInArray(arr):
    actual_sum = sum(arr)
    n = len(arr)
    return (n * (n + 1) // 2) - actual_sum


def SubStringInString(needle, haystack):
    if len(needle) > len(haystack):
        return -1
    n = len(haystack)
    m = len(needle)
    for i in range(n - m + 1):
        if haystack[i: i+m] == needle:
            return i
    return -1


def Sum2LinkedList(ll1, ll2):

    def create_node(ll, key):
        new_node = None
        new_node.key = key
        new_node.next = None
        return new_node

    head1 = ll1
    head2 = ll2
    carry = 0
    dummy_ll = None
    dummy_ll_curr = None

    while ll1 or ll2 or carry > 0:
        key_1 = ll1.key if ll1 else 0
        key_2 = ll2.key if ll2 else 0
        final_sum = key_1 + key_2 + carry
        carry = final_sum // 10
        final_sum = final_sum % 10
        new_node = create_node(dummy_ll, final_sum)
        if dummy_ll:
            dummy_ll_curr.next = new_node
        else:
            dummy_ll = new_node

        dummy_ll_curr = new_node

        if ll1 is not None:
            ll1 = ll1.next
        if ll2 is not None:
            ll2 = ll2.next
        return dummy_ll

    def CopyLinkedListWithArbitrary(self):
        head = self.head
        if not head:
            return -1
        current = head
        while current:
            cloned_node = Node(current.key)
            cloned_node.next = current.next
            current.next = cloned_node
            current = cloned_node.next

        current = head
        while current:
            if current.arbitrary:
                current.next.arbitrary = current.arbitrary.next
            current = current.next.next

        current = head
        cloned_node = head.next
        while current:
            cloned_node = current.next
            current.next = cloned_node.next
            current = current.next
            if cloned_node.next:
                cloned_node.next = cloned_node.next.next

        return cloned_node


# SumOf3IntegerSameAsTarget([1, 3, 4, 5, 6, 5, 5], 15)
print(SubStringInString("Am", "IAmSad"))
