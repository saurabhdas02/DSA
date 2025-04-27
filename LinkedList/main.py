class Node:
    head = None

    def __init__(self, key, arbitrary=None):
        self.key = key
        self.next = None
        self.arbitrary = arbitrary
        if self.head is None:
            self.head = self

    def insertAtStart(self, key):
        new_node = Node(key)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def deleteFromStart(self, key):
        if self.head is None:
            return None
        else:
            tmp = self.head.next
            self.head = self.head.next
            del tmp

    def InsertAtIndex(self, key, index):
        if index == 0:
            self.insertAtStart(key)
        else:
            new_node = Node(key)
            curr = self.head
            curr_index = 1
            while curr is not None and curr_index < index - 1:
                print(curr.key)
                curr = curr.next
                curr_index += 1

            if curr is not None:
                new_node.next = curr.next
                curr.next = new_node

    def InsertAtEnd(self, key):
        new_node = Node(key)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next

            curr.next = new_node

    def searchKey(self, key):
        current = self.head
        index = 1
        while current is not None:
            if current.key == key:
                return index
            index += 1
            current = current.next
        return -1

    def printNthElement(self, nth_index):
        tmp = self.head
        counter = 1
        while tmp is not None and counter <= nth_index-1:
            tmp = tmp.next
            counter += 1
        if tmp is not None:
            print(f"{nth_index}th_index value: {tmp.key}")
        else:
            print("-1")

    def printList(self):
        if self.head is None:
            print("Empty Linked List")
        else:
            tmp = self.head
            while tmp is not None:
                print(tmp.key)
                tmp = tmp.next

    def printNthFromEnd(self, index):
        len = 0
        curr = self.head
        while curr:
            curr = curr.next
            len += 1

        if len < index:
            return -1

        curr = self.head
        for i in range(1, len-index+1):
            curr = curr.next
        print(f"{index}th_index value: {curr.key}")

    def printNthFromEndAdvanced(self, n):
        dummy = Node(0)  # Create a dummy node to handle edge cases
        dummy.next = self.head  # Connect dummy node to the head of the list
        first = dummy
        second = dummy

        # Move the first pointer n steps ahead
        for _ in range(n + 1):
            first = first.next

        # Move both pointers together until first reaches the end
        while first is not None:
            first = first.next
            second = second.next

        # Remove the nth node from the end
        second.next = second.next.next

        return dummy.next  # Return the head of the modified list

    def deleteElement(self, target):
        curr = self.head
        prev = None

        while curr is not None and curr.key != target:
            prev = curr
            curr = curr.next

        if curr is None:
            print("No Delete")
        else:
            prev.next = curr.next
            del curr
            self.printList()

    def removeDuplicatesFromSortedLL(self):
        curr = self.head
        while curr.next is not None:
            if curr.key == curr.next.key:
                curr.next = curr.next.next
            else:
                curr = curr.next

    def reverseLL(self):
        curr = self.head
        prev = None
        while curr is not None:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        self.head = prev
        self.printList()

    @classmethod
    def merge2LinkedList(cls, head1, head2):
        answer_head = Node(-1)
        tail = answer_head
        while head1 is not None and head2 is not None:
            if head1.key < head2.key:
                tail.next = head1
                head1 = head1.next
                tail = tail.next
                tail.next = None
            else:
                tail.next = head2
                head2 = head2.next
                tail = tail.next
                tail.next = None
            if not (head1 is None and head2 is None):
                if head1 is None:
                    tail.next = head2
                else:
                    tail.next = head1

        while answer_head is not None:
            print(answer_head.key)
            answer_head = answer_head.next

    def checkPalindromeLL(self):
        from collections import deque
        stack = deque()
        tmp = self
        while tmp:
            print(tmp.key)
            stack.append(tmp.key)
            tmp = tmp.next
        tmp = self
        while tmp:
            return print("Not palindrome") if tmp.key != stack.pop() else print("True")

    @classmethod
    def getIntersectionNode(cls, head1, head2):
        dummy1 = head1.head
        dummy2 = head2.head
        while dummy1 != dummy2:
            dummy1 = dummy1.next if dummy1 else head2.head
            dummy2 = dummy2.next if dummy2 else head1.head

        return dummy1

    @classmethod
    def getIntersectionNodeAlternate(cls, head1, head2):
        def get_length(head):
            counter = 0
            while head:
                counter += 1
                head = head.next
            return counter

        len_1 = get_length(head1)
        len_2 = get_length(head2)

        while len_1 > len_2:
            head1 = head1.next
            len_1 -= 1
        while len_2 > len_1:
            head2 = head2.next
            len_1 -= 1

        while head1 and head2:
            if head1 == head2:
                return head1
            head1 = head1.next
            head2 = head2.next
        return None

    def middleOfLL(self):
        slow, fast = self.head, self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def detectCycleInLL(self):
        slow = self.head
        fast = self.head
        if not self.head or self.head.next:
            return False
        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next
        return False

    def reverseBetweenLL(self, left, right):
        head = self.head
        if not head or not head.next:
            return head
        dummy = Node(0)
        dummy.next = head
        prev = dummy
        # Move `prev` to the node just before the `left` position
        for _ in range(left - 1):
            prev = prev.next
        curr = prev.next
        # Reverse the nodes between `left` and `right`
        for _ in range(right - left):
            temp = prev.next
            prev.next = curr.next
            curr.next = curr.next.next
            prev.next.next = temp
        return dummy.next

    def CopyLinkedListWithArbitrary(self):
        head = self.head
        if not head:
            return -1
        current = head
        while current:
            new_node = Node(current.key)
            new_node.next = current.next
            current.next = new_node
            current = new_node.next

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




